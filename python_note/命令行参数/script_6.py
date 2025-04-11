import argparse
# 默认情况下，argparse 将提供的选项视为字符串。
# 因此，如果参数不是字符串，则应使用 type 选项。
# 添加了两个参数，这两个参数是 int 类型
parser = argparse.ArgumentParser()
parser.add_argument("first_number", help="first number to be added", type=int)
parser.add_argument("second_number", help="second number to be added", type=int)
args = parser.parse_args()
print("args: '{}'".format(args))
print("the sum is: '{}'".format(args.first_number + args.second_number))
# vars() 函数返回对象object的属性和属性值的字典对象
args_dict = vars(parser.parse_args())
print("args_dict dictionary: '{}'".format(args_dict))
print("first argument from the dictionary: '{}'".format(args_dict["first_number"]))
