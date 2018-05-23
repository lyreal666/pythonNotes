#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#列表生成式
# 1.结果是个列表
# 2.要生成的表达式放在最前面
# 3.一切普通for in循环能用的在listConprehensions中都能用
# 4.允许多个for循环，使用多个循环时，效果是全排列形式
# 5.使用rang（）函数

print(range(1,11))#range函数返回一个range对象
print([range(1,11)])#含有一个rang对象元素的list
print(list(range(1,11)))

conbineStr = ""
for i in list(range(1,11)) :
	conbineStr += str(i) + " * " + str(i + 1) + "	"
print(conbineStr)

tlis = []
for i in range(1,11) :
	tlis.append(i * i)

print(tlis)
#当目的是为了生成一个列表，考虑用列表生成式
#列表生成式是从空表到按规则生成列表的过程
print([i * i for i in range(1,11)])
print([(str(i) + ' * ' + str(i + 1)) for i in range(1,11)])

ttup = (1,2,3,4)
print([i ** i for i in ttup])

print("1-3可重复所有排列：",
[str(i) + str(j) + str(k)  for i in range(1,4) for j in range(1,4) for k in range(1,4)])

print("1-3全排列：",
[str(i) + str(j) + str(k)  for i in range(1,4) for j in range(1,4) for k in range(1,4)
if i != j and i != k and j != k])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# def triangles() :
# 	l2 = []
	
# 	for i in range(1,11) :
# 		if i == 1 :
# 			l2.append([1])
# 			yield ([1])
# 		else :
# 			l2.append([1,1])

# 	yield ([1,1])

# 	for i in range(2,10) :
# 		for j in range(1,i) :
# 			newEle = l2[i - 1][j] + l2[i - 1][j - 1]
# 			l2[i].insert(j,newEle)

# 		yield(l2[i])

# 	return "done"

def triangles() :
	max = 10
	list3 = [1]
	num = 0

	while num < max :
		yield (list3)
		list4 = list(list3)
		list4.insert(0,0)
		list4.append(0)

		list3 = [(list4[i] + list4[i + 1]) for i in range(len(list4) - 1)]
		num  += 1

	return 'done'

print(triangles())
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')	

		

