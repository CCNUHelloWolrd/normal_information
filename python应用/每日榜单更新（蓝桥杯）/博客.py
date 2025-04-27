# 容我发了一篇博客

# todo: 代码流程：
#  手动：
#       登录洛谷账号，找到比赛榜单的网址，并找到账号cookie
#       在下方对应位置更替内容
#  自动：
#       根据cookie依次向洛谷平台请求网址中的数据
#       将请求到的数据储存（可视化可选）


import requests
import pandas as pd
import json

# 提前设定输出格式
pd.set_option('display.max_columns', None)  #显示所有列
pd.set_option('display.max_rows', None) #显示所有行
pd.set_option('max_colwidth', 100)   #设置value的显示长度为100


def get_data(url_id, cookie):
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
        write_data(url_id, data)    # 保存JSON数据
        show_contest_sig(data)  # 展示JSON数据
        return data
    else:
        print(f'请求失败。状态码: {response.status_code}')
        print(f'响应内容: {response.text}')
        return False


def write_data(url_id, data):
    """将json数据以易读的形式储存"""
    with open(f'luogu_contest_{url_id}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


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
    print(df)


# todo: 以下内容需更改
#  cookies 改成自己账号的
#  inf 请自己添加
cookies = {
    "__client_id": "*******",
    "_uid": "******",
    "C3VK": "******",
}

inf = {
    '比赛1': '******',
    '比赛2': '******',
}

for key, value in inf.items():
    print(f"正在爬取榜单{key}内容！")
    get_data(url_id=value, cookie=cookies)
