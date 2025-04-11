import sys
import getopt

"""
在参数列表中没有找到所传递参数，或选项的需要的参数为空时会触发该异常。
异常的参数是一个字符串，表示错误的原因。
属性 msg 和 opt 为相关选项的错误信息。

"""

def main(argv):
    input_file = ""
    output_file = ""
    try:
        opts, args = getopt.getopt(argv[1:], "hi:o", ["help", "input_file=", "output_file="])

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
            print(f"不含' - '或' - -'的参数 {i + 1} 为：{args[i]}")

    except getopt.GetoptError as e:
        print(e.msg)
        print(e.opt)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv)