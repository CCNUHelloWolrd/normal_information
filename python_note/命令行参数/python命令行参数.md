## 命令行参数
[学习链接](https://blog.csdn.net/LOVEmy134611/article/details/119656854)

对于大型项目程序而言，执行程序的一个必要的步骤是正确处理命令行参数，
这些命令行参数是提供给包含某种参数化信息的程序或脚本的参数。

例如，在计算机视觉项目中，图像和不同类型的文件通常作为命令行参数传递给脚本，
用于使程序可以处理不同图片或者不同类型文件。

命令行参数是参数化程序执行的一种常见且简单的方法。

## 常见的获取和解析命令行参数的方法
### sys.argv

sys.argv 可以访问到所有的命令行参数，注意内容格式

内容参照脚本 script_1.py

运行以下命令行来观察区别(**注意地址**)：

    python script_1.py
    python script_1.py OpenCV -i test.png

###  getopt

方法：getopt.getopt(args, options[, long_options])

注意**命令行参数的短格式分析串、长格式分析串列表**，输出格式

内容参照脚本 script_2.py

命令行选项的命令执行此脚本进行观察(**注意地址**)：

    python scripy_2.py -i test.png -o output.png OpenCV
    python scripy_2.py --input_file test.png --output_file output.png OpenCV

***报错处理***

内容参照脚本 script_3.py

命令行选项的命令执行此脚本进行观察(**注意地址**)：

    python scripy_3.py -f -i 

观察到：
    
    C:\Users\86152>python script_3.py -g -i
    option -g not recognized
    g
    
    C:\Users\86152>python script_3.py -i
    option -i requires argument
    i

### argparse

内容参照脚本 script_4.py、script_5.py、script_5.py

命令行选项的命令执行此脚本进行观察(**注意地址**)：

script_4.py 没有设定任何接受参数

    python scripy_4.py
    python scripy_4.py -h
    python scripy_4.py -i

script_5.py 设定接受参数 first_argument 
    
    python scripy_5.py 10
    python scripy_5.py 
    python scripy_5.py -h

script_6.py 设定接受参数的数据类型

    python scripy_6.py 10 100
    python scripy_6.py 
    python scripy_6.py -h

进一步学习请查看[**官方文档**](https://docs.python.org/3/howto/argparse.html)

结论： 默认设定选项-h，必须符合参数预设

## 结论
在大项目中，利用命令行快速调用脚本进行数据处理，通过这三个方式来了解命令行是怎么编写、执行的。
以后的代码中，命令行参数可以作为项目的一部分来使用。