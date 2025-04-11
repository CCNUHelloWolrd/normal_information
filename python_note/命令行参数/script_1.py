"""
模块中的 sys.argv 就可以访问到所有的命令行参数，它的返回值是包含所有命令行参数的列表 (list)
当程序执行时，Python 从命令行获取所有值并将它们存储在 sys.argv 列表中。
列表的第一个元素 sys.argv[0] 是脚本的完整路径(或脚本名称——取决于具体操作系统)。
列表的第二个元素是脚本的第一个命令行参数，即 sys.argv[1]，依此类推。

"""
import sys
print("正在运行的脚本名称: '{}'".format(sys.argv[0]))
print("脚本的参数数量: '{}'".format(len(sys.argv)))
print("脚本的参数: '{}'".format(str(sys.argv)))

