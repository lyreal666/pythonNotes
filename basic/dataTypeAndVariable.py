#string
#python数据类型
# 1.整形
# 2.str
# 3.float
# 4.bool
# 5.bytes


import sys
print('hello')
print("world")
print("I'm LY")
print("老余")
print("老余")
print('''床前明月光
疑是地上霜
举头望明月
低头思故乡''')#使用三个点换行不用加换行符

#bool 都是大写(Ture,False)
print(1 > 2,2 > 1)
if True and True:
	print("and 运算符 同时为真才真")

if not False:
	print("非运算")

if False or False:
	print("同假才假")
elif True or False:
	print("有一个真就真")
else:
	sys.getdefaultencoding()

print(sys.getdefaultencoding())

#空值
print(None)

#除法
print(6 / 4)
print(6 // 4)
print(8 % 4)