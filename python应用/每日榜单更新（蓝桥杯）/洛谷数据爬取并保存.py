import requests
import pandas as pd
import json

# todo: 代码流程：
#  手动：
#       登录洛谷账号，找到比赛榜单的网址，并找到账号cookie
#       在下方对应位置更替内容
#  自动：
#       根据cookie依次向洛谷平台请求网址中的数据
#       将请求到的数据储存（可视化可选）

# todo: 注意最后需要更改内容

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# #设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)


def get_data(url_id, cookie, date=0):
    """请求数据"""
    # API 接口URL
    api_url = f'https://www.luogu.com.cn/fe/api/contest/scoreboard/{url_id}?page=1'
    # 请求头（标准）（反爬虫）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Referer': 'https://www.luogu.com.cn/contest/list',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # 使用requests发送GET请求，并将相应结果储存在response中
    response = requests.get(api_url, headers=headers, cookies=cookie, timeout=10)

    # 判断相应结果
    if response.status_code == 200:
        print('成功获取数据！')
        data = response.json()  # 解析JSON数据
        write_data(url_id, data, date=date)    # 保存JSON数据
        # show_contest_sig(data)          # 展示
        change_data_type(url_id, data, date=date)   # 改变格式并储存
        return data
    else:
        print(f'请求失败。状态码: {response.status_code}')
        print(f'响应内容: {response.text}')
        return False


def write_data(url_id, data, date=0):
    """将json数据以易读的形式储存"""
    with open(f'luogu_contest_{url_id}_{date}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("原始数据已保存")
    # todo: 2024、2025年榜单绘制的数据为复制粘贴，
    #  2025年活动快结束的时候，完成自动爬虫，
    #  但是爬虫的数据格式与复制的数据格式不同，
    #  请后来者自行转换
    #  不要怕，很简单


def show_contest_sig(data):
    """绘制一个比赛的榜单"""
    # 提取排行榜数据
    # json是多维字典，这里仅需['scoreboard']['result']对应的值
    new_data = data['scoreboard']['result']
    # 将数据转换为 DataFrame
    # todo: enumerate迭代器遍历new_data的值
    #  '排名'、'用户名'、'总分'、result['details'].keys() 为列索引
    #  ** 为解包，就是将字典的{}去掉，里面的元素提取出来
    #  :后面对应每一列将要显示的数据
    df = pd.DataFrame([
        {
            '排名': idx + 1,
            '用户名': result['user']['name'],
            '总分': result['score'],
            **{f'题目 {problem}': details['score'] for problem, details in result['details'].items()}
        }
        for idx, result in enumerate(new_data)
    ])

    # 打印表格
    print("数据可视化如下")
    print(df)


def change_data_type(url_id, data, date=0):
    with open(f'luogu_contest_{url_id}_{date}.json', 'r', encoding='utf-8') as swap_file:
        swap_data = json.load(swap_file)
    new_data = swap_data['scoreboard']['result']
    with open("比赛信息.txt", 'w+', encoding="utf-8") as file:
        for id, result in enumerate(new_data):

            # 因团队名与洛谷账号名位置不同，部分成员不改名，导致报错，故加此段处理
            try:
                if result['teamMember']['realName']:
                    file.write(f"#{id + 1}\t{result['teamMember']['realName']}\t{result['score']}\n")
            except:
                file.write(f"#{id + 1}\t{result['user']['name']}\t{result['score']}\n")

            for details in result['details'].values():
                file.write(f"({details['runningTime']})\t{details['score']}\n")
    print("数据格式已转换")
    print("转换数据已保存在 比赛信息.txt")


# todo: 以下内容需更改
#  cookies 改成自己账号的
#  inf 请自己添加
#  date 为日期，请更新
cookies = {
    "__client_id": "c82a6499137adf51dd925b115655ac9dc0ead305",
    "_uid": "903615",
    "C3VK": "80db82",
}

inf = {
    '新手练习':'224852',
    '基础练习':'224225',
}
date = "2025_2_4"

# 删除历史数据
with open("比赛信息.txt", 'w', encoding="utf-8") as file:
    print("初始化 比赛信息.txt")

for key, value in inf.items():
    print(f"正在爬取榜单{key}内容！")
    get_data(url_id=value, cookie=cookies, date=0)