#!flask/bin/python
from app import app  #导入app文件中__init__中app=Flask(__name__)
#1）当文件是被调用时，__name__的值为模块名；
#2）当文件被执行时，__name__的值为 ‘__main__’。
#基于此特性，为测试驱动开发提供了很好的支持，我们可以在每个模块中写上测试代码
#这些测试代码仅当模块被Python直接执行时才会运行，代码和测试完美的结合在一起。
#
app.debug = True  #设置debug模式
app.run() #link start