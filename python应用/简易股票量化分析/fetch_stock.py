import akshare as ak
import pandas as pd
import numpy as np
import time
import os
from typing import Callable, Any
import requests

# ==================== 通用重试装饰器 ====================
def retry_with_backoff(max_retries: int = 4, initial_sleep: float = 2.0):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            retries = 0
            sleep_sec = initial_sleep
            while retries <= max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.ConnectionError as e:
                    retries += 1
                    if retries > max_retries:
                        raise e
                    print(f"网络异常，第{retries}次重试，等待{sleep_sec:.1f}s: {str(e)[:140]}")
                    time.sleep(sleep_sec)
                    sleep_sec *= 2
                except Exception as e:
                    raise e
        return wrapper
    return decorator

# ==================== 新浪源日K stock_zh_a_daily（必须 sz/sh） ====================
@retry_with_backoff(max_retries=4, initial_sleep=2.0)
def _fetch_stock_daily_net(sina_symbol: str) -> pd.DataFrame:
    """
    新浪源日K，sina_symbol: "sz002575" 必须带sz/sh前缀
    接口返回全部历史，本地再做时间切片
    """
    print(f"    新浪拉取 {sina_symbol} 全部日K历史")
    df_raw = ak.stock_zh_a_daily(symbol=sina_symbol, adjust="")
    time.sleep(1.5)

    if df_raw.empty:
        raise ValueError(f"{sina_symbol} 新浪日K接口返回空数据")

    df_raw["date"] = pd.to_datetime(df_raw["date"])
    df_raw = df_raw.set_index("date")
    # 计算日度vwap
    df_raw["vwap"] = df_raw["amount"] / df_raw["volume"]
    return df_raw


def fetch_stock_daily(sina_symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    带缓存：新浪全量拉取，本地切片到 start_date ~ end_date
    sina_symbol: "sz002575"
    """
    cache_filename = f"cache_sina_daily_{sina_symbol}.parquet"
    if os.path.exists(cache_filename):
        print(f"[缓存命中] 读取新浪日K缓存：{cache_filename}")
        df_full = pd.read_parquet(cache_filename)
    else:
        print(f"[缓存未命中] 联网拉取新浪 {sina_symbol} 日K...")
        df_full = _fetch_stock_daily_net(sina_symbol)
        df_full.to_parquet(cache_filename)
        print(f"[保存缓存] 写入 {cache_filename}")

    # 本地时间切片
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)
    df = df_full.loc[(df_full.index >= start_dt) & (df_full.index <= end_dt)].copy()
    if df.empty:
        raise ValueError(f"{sina_symbol} 切片后时间区间 {start_date}~{end_date} 无数据")
    return df

# ==================== 黄金（上金所 Au99.99） ====================
@retry_with_backoff(max_retries=4, initial_sleep=2.0)
def _fetch_gold_data_net() -> pd.DataFrame:
    print("    调用上金所Au99.99接口")
    df_gold = ak.spot_hist_sge(symbol="Au99.99")
    time.sleep(1.2)

    if df_gold.empty:
        raise ValueError("Au99.99 获取空黄金数据")

    df_gold["date"] = pd.to_datetime(df_gold["date"])
    df_gold = df_gold.set_index("date")[["close"]].rename(columns={"close": "gold_cny_g"})
    return df_gold


def fetch_gold_data():
    cache_filename = "cache_gold_Au9999.parquet"
    if os.path.exists(cache_filename):
        print(f"[缓存命中] 读取黄金本地缓存：{cache_filename}")
        df = pd.read_parquet(cache_filename)
        return df

    print("[缓存未命中] 联网拉取Au99.99黄金数据 ...")
    df = _fetch_gold_data_net()
    df.to_parquet(cache_filename)
    print(f"[保存缓存] 黄金数据写入 {cache_filename}")
    return df

# ==================== 日K黄金本位 σ 分析主函数 ====================
def compute_daily_gold_analysis(
        sina_symbol: str,
        stat_start: str,
        stat_end: str
):
    df_daily = fetch_stock_daily(sina_symbol, stat_start, stat_end)
    df_gold = fetch_gold_data()

    df_gold_aligned = df_gold.reindex(df_daily.index).ffill().dropna()
    df_full = pd.concat([df_daily, df_gold_aligned], axis=1, join="inner")
    df_full = df_full.dropna()

    if df_full.empty:
        raise RuntimeError("日K与Au9999黄金对齐后数据为空，检查时间区间")

    df_full["vwap_gold"] = df_full["vwap"] / df_full["gold_cny_g"]
    df_full["close_gold"] = df_full["close"] / df_full["gold_cny_g"]

    # 成交量加权黄金本位均价
    total_vwap_gold = (df_full["vwap_gold"] * df_full["volume"]).sum() / df_full["volume"].sum()
    sigma_gold = np.std(df_full["vwap_gold"].values, ddof=0)

    m = total_vwap_gold
    s = sigma_gold
    boundaries = {
        "-3σ": m - 3 * s,
        "-2σ": m - 2 * s,
        "-1σ": m - 1 * s,
        "+1σ": m + 1 * s,
        "+2σ": m + 2 * s,
        "+3σ": m + 3 * s,
    }

    def get_sigma_zone(val: float) -> str:
        if val < boundaries["-3σ"]:
            return "< -3σ"
        elif val < boundaries["-2σ"]:
            return "-3σ ~ -2σ"
        elif val < boundaries["-1σ"]:
            return "-2σ ~ -1σ"
        elif val < boundaries["+1σ"]:
            return "-1σ ~ +1σ"
        elif val < boundaries["+2σ"]:
            return "+1σ ~ +2σ"
        elif val < boundaries["+3σ"]:
            return "+2σ ~ +3σ"
        else:
            return "> +3σ"

    df_full["sigma_zone"] = df_full["vwap_gold"].apply(get_sigma_zone)

    result_dict = {
        "stock_code": sina_symbol,
        "stat_start": stat_start,
        "stat_end": stat_end,
        "total_vwap_gold_weighted": total_vwap_gold,
        "sigma_gold": sigma_gold,
        "boundaries": boundaries,
        "total_bar_count": len(df_full),
        "last_trade_date": df_full.index[-1].date()
    }
    return result_dict, df_full


def main(sina_symbol: str, stat_start: str, stat_end: str):
    res, df_full = compute_daily_gold_analysis(sina_symbol, stat_start, stat_end)

    print("=" * 70)
    print(f"股票:{res['stock_code']}  统计区间:{res['stat_start']} ~ {res['stat_end']}")
    print(f"统计区间日K总数：{res['total_bar_count']}")
    print(f"黄金本位成交量加权总均价 = {res['total_vwap_gold_weighted']:.6f} 克/股")
    print(f"区间总体标准差 σ        = {res['sigma_gold']:.6f}")
    print("σ 边界：")
    for k, v in res["boundaries"].items():
        print(f"    {k:>4} : {v:.6f}")
    print(f"\n最后交易日：{res['last_trade_date']}")
    print("【最后5天 vwap_gold 与 σ区间】")
    print(df_full[["vwap_gold", "close_gold", "sigma_zone"]].tail(5).to_string())

    df_full.to_csv("daily_gold_sigma.csv", encoding="utf-8-sig")
    print("\n已输出：daily_gold_sigma.csv")
    return res, df_full


if __name__ == "__main__":

    main('sz002575', '20260701', '20260901')
