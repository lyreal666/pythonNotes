#!/usr/bin/env python3
# -*- coding:utf-8 -*-

print(list(range(10)))
#------------------dict-------------------#
dic = {'plus':'+','minus':'-','muitiply':'*','divides':'//'}

print(dic)

print('spring' in dic)

dic['model'] = '%'
dic.pop('model')
for d in dic :
	print(d + ':',dic.get(d,'not exits'))


#-----------------set--------------------------#
#in操作符对set无效
#set可以用来过滤数据
set1 = set(['spring','summer','autumn','winter'])

for s in set1 :
	print(s)

set1.add('fall')
set1.add('fall')
set1.remove('fall')

print(set1)

#数学意义上的集合
set_a = set([1,2,3,4])
set_b = set([3,4,5,6])

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
# 没+运算

var1 = 4
var2 = 4

print(id(var1))
print(id(var2))

print(var1 is var2)
print(var1 is not var2)
var1 = 5
print(id(var1))

list1 = ['a','b','c','d']
list2 = ['h','j','k','l']
print('a' in list1)
print('h' not in list2)

from collections import Iterable
#迭代器
def findMinAndMax(L) :
	if isinstance(L,Iterable) and len(L) >= 1 :
		max = L[0];
		min = L[0];

		for v in L :
			if v > max :
				max = v

			if v < min :
				min = v

		return (min,max)

	else:
		return (None,None)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


ilist1 = ['w','a',7,8]

for order,value in enumerate(ilist1):
	print(str(order) + ':' , value)

tdict = {"spring":"春","summer":"夏","autumn":"秋","winter":"冬"}
for key,value in tdict.items() :
	print(key + ':',value)

for value in tdict.values() :
	print(value)

for a,b in [['key1','value1'],('key2','value2')] :
	print(a,b)

tlist = list(range(100))

print(tlist[:10])
print(tlist[2:12:2])
print(tlist[-2:-1])
print(tlist[-3:])
print("abcde"[-3:])
print("abcde"[::2])