from app.love_pyramid import love_pyramid
from app.tricards import tricards

def interact():
    holy = input('敲击你最想按的一个或几个键建立链接')
    print('''
    1.恋人金字塔
    2.大三角
    ''')
    x = input('请输入想要使用的牌阵的编号：')
    if x == '1':
        love_pyramid()
    elif x=='2':
        tricards()