#下面这一行告诉linux系统这是一个可执行程序，可以在命令行直接敲文件名运行
#!/usr/bin/env python3

#下面这一行指定源代码编写方式
# -*- coding: utf-8 -*-

print('''众里寻他千百度
那人却在灯火阑珊处''')
print("str:%5s digtal:%3d float:%.2f" % ("abcde",12,3.14159))
print("str:%5s digtal:%03d float:%.2f" % ("abcde",12,3.14159))

#prac1
scoreLast = 72
scoreThisYear = 85
rate  = (85 - 72) / 72
#使用%格式化字符串时%字符用%%转译，format函数不需要
print("%")
print("the progress percent point is {0:.1f}%".format(rate))
print("the progress percent point is %.1f%%" %rate)

#Python还允许用r''表示''内部的字符串默认不转义
print(r"\\\\t")

#使用ord和chr函数获取对应字符整数编码和整数对应字符
print(ord('A'))
print(chr(65))
print(chr(25991))

#字符的整数编码，还可以用十六进制这么写str：
print("\u4e2d\u6587")

#Python对bytes类型的数据用带b前缀的单引号或双引号表示
print(b"abc")
print(len(b'abc')) -

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('中国'.encode("utf-8"))
print('ABC'.encode('ascii'))

#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
#要把bytes变为str，就需要用decode()方法
print(b'abc'.decode('ascii'))
print(b"\xe4\xb8\xad\xe5\x9b\xbd".decode('utf-8'))

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b"\xe4\xb8\xad\xe5\x9b\xff".decode("utf-8",errors = "ignore"))