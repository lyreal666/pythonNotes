#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"test rtti or attribute of class"

__author__ = "LY"

#------------------id函数-----------------#
#使用id()函数
ivar = 9
fvar = 9
fvar1 = 9.0
print(id(ivar))
print(id(fvar))
print(id(fvar1))
#is 操作符 a is b 相当于 id(a) == id(b)
print( ivar is fvar)
print(ivar is not fvar1)

#---------------------type函数------------------------#
import types
print(type(int))

fvar1 = 1.0
print(type(fvar1))

def compare(x,y):
	return x if x >= y else y
print(type(compare))

class Base(object):
	pass

class Devired(Base):
	pass
print(type(len) == types.BuiltinFunctionType)
print(type(lambda x: x if x >= 0 else -x) == types.LambdaType)
print(type(compare) == types.FunctionType)

b = Base()
d = Devired()

print(type(b))		
print(type(d))

print(isinstance(b,Base))
print(isinstance(d,Base))
#使用isinstance会时子类会被视为和父类同一类
#所以在对父类进行类型检查时应当使用isinstance而不是type

#---------------------------dir函数------------------------------#
#一个下划线开头只是其提示作用
#2个下划线开头外部访问时有所限制一般会修改参数名如__func -> _MyObject__func
print(dir(int))

class MyObject:
	def __init__(self):
		self.x = 0
		self.__x = 1
		self.__y = 2

	def power(self):
		return self.x * self.x

	def p__x(self):
		print(self.__x)

obj = MyObject()
print(type(obj))
print(isinstance(obj,MyObject))
print(dir(obj))

#3个有用的bif getattr,serattr,hasattr
print(hasattr(obj,'x'))
print(hasattr(obj,'power'))

setattr(obj,'x',10)
print(obj.x)
setattr(obj,'__x',10)
obj.p__x()
obj.__x = 11
print(dir(obj))

print(getattr(obj,"_MyObject__y"))
pf = getattr(obj,'p__x')
pf()