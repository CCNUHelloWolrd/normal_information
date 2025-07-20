
from app import *

with open('./data/read.txt', 'r', encoding='utf-8') as file:
    print(file.read())
if __name__ == '__main__':
    interact()
else:
    print('文件损坏')