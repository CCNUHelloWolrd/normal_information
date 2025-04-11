"""
getopt 模块是专门处理命令行参数的模块，用于获取命令行选项和参数。
命令行选项使得程序的参数更加灵活，其支持短选项模式(-)和长选项模式(–)
"""
# getopt.getopt(args, options[, long_options])
# args	要解析的命令行参数列表，一般是sys.argv[1:]，需要过滤掉脚本名(sys.argv[0])
# options	以字符串的格式定义，options 后的冒号 “:” 表示如果设置该选项，必须有附加的参数，否则就不附加参数
# long_options	以列表的格式定义，long_options 后的等号 “=” 表示该选项必须有附加的参数，不带冒号表示该选项不附加参数
# 该方法返回值由两个元素组成:
# 第一个是 (option, value) 元组的列表。
# 第二个是参数列表，包含那些没有 - 或 – 的参数。
import sys
import getopt


def main(argv):
    input_file = ""
    output_file = ""
    # "hi:o:": 短格式分析串, h 后面没有冒号, 表示后面不带参数; i 和 o 后面带有冒号, 表示后面带参数
    # ["help", "input_file=", "output_file="]: 长格式分析串列表, help后面没有等号, 表示后面不带参数; input_file和output_file后面带冒号, 表示后面带参数
    # 返回值包括 `opts` 和 `args`, opts 是以元组为元素的列表, 每个元组的形式为: (选项, 附加参数)，如: ('-i', 'test.png');
    # args是个列表，其中的元素是那些不含'-'或'--'的参数
    opts, args = getopt.getopt(argv[1:], "hi:o:", ["help", "input_file=", "output_file="])

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('script_2.py -i <input_file> -o <output_file>')
            print('or: test_arg.py --input_file=<input_file> --output_file=<output_file>')
            sys.exit()
        elif opt in ("-i", "--input_file"):
            input_file = arg
        elif opt in ("-o", "--output_file"):
            output_file = arg
    print('输入文件为：', input_file)
    print('输出文件为：', output_file)

    # 打印不含'-'或'--'的参数
    for i in range(0, len(args)):
        print(f"不含' - '或' - -'的参数 {i + 1} 为：{args[i]}" )


if __name__ == "__main__":
    main(sys.argv)
