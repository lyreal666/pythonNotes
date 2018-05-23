#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 记住，python在定义函数时是不需要声明类型的
#---------------------普通函数-----------------------#
def bigger(x,y):
	if not isinstance(x,(int,float)) or not isinstance(y,(int,float)) :
		raise TypeError("type error")
	else :
		if x >= y :
			return x
		else :
			return y

print(bigger(8,7))

def ret_element(ls) :
	if len(ls) >= 2 :
		return ls[0],ls[1]
	elif len(ls) == 1 :
		return ls[0]
	else :
		print("none")

ls = [1,2]
tup = ret_element(ls)
#tup[1] = 2说明返回的是t
print(tup[1])
print(ret_element([3,4]))

#----------------特殊参数-------------------#
#x叫位置参数，n叫默认参数
def power(x, n = 2) :
	res = 1
	while n != 0 :
		res *= x
		n -= 1

	return res

print(power(2))
print(power(2,3))

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


def recoding_exception(_time,num,managerName = "Ly",*argc,exceptionCount,**kw) :
	print('time:',_time)
	print('number:',num)
	print('managerName', managerName)

	for e in argc :
		print('exception:',e)	

	print('exceptionCount,',exceptionCount)

	for d in kw :
		print(d + ':',kw[d])

exceptions = ['OutBoundException','NumberFormatException','RunTimeExceptio']
dic = {'resut':'in not ba','report':"can't happen"}
recoding_exception('10:28',111,'LY',*exceptions,exceptionCount = 3,**dic)

def move(n,a,b,c) :
	if n == 1 :
		print(a,'->',c)
	else :
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(3,'A','B','C')

def trim(sstr) :
	beg = 0
	end = len(sstr) - 1
	index = 0

	while index != end + 1 and sstr[index] == ' ' :
		index += 1

	if index == end + 1 :
		return ''
	else :
		beg = index
		index = end

	while index != beg -1 and sstr[index] == ' ' :
		index -= 1

	if index != beg - 1 :
		end = index + 1
		return sstr[beg:end]
	else :
		return ''

	

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')