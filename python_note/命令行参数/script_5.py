"""
当程序中使用采用复杂参数或多个文件名时，推荐使用 Python 的 argparse 库，
它以系统的方式处理命令行参数，从而可以编写用户友好的命令行程序。
Python 标准库 argparse 同样也是用于解析命令行参数的模块。
首先，由程序确定所需的参数，然后， argparse 将这些参数解析为 sys.argv。
此外，argparse 会生成帮助和使用信息提示，并在提供无效参数时发出错误。

"""

import argparse

parser = argparse.ArgumentParser()
# add_argument() 方法。
#  此方法用于指定程序将接受哪些命令行选项，此处添加了 first_argument 参数。
# argparse 模块存储所有参数，
#  将其名称与每个添加参数的名称相匹配——在此处为 first_argument 。
#  为了获得参数值，需要使用 args.first_argument
parser.add_argument("first_argument", help="this is the string text in connection with first_argument")
args = parser.parse_args()
print(args.first_argument)