#!usr/bin/env python3
# -*- coding： utf-8 -*-

#-------------------------list-------------------------#
#定义以及增删改,索引
listdemo = ["春",'夏','秋','冬']
print(listdemo)

listdemo.append('spring')
print(listdemo)
listdemo.insert(1,'summer')
print(listdemo)

listdemo.pop()
print(listdemo)
listdemo.pop(1)
print(listdemo)

listdemo[0] = 'spring'
print(listdemo)
listdemo[0] = '春'
print(listdemo)

print(listdemo[0])
print(listdemo[3])
print(listdemo[-1])#使用-号反向索引,-1表示反向第一个
print(listdemo[-4])

#List可以类型不唯一，可以用多维数组形式使用list
ls = [1,'2',0.3,listdemo]
print(ls)
print(ls[3][1])

#空list
emptyList = []

#----------------------tuple(元组)-----------------------------#
#一句话:tuple是存放对每个元素的指针的list，并且指针不变,元素个数不变
tup = ('earth','moom','mars')
print(tup)

#最有读操作
print(tup[0])
print(tup[-1])

#注意只有一个元素的情况
tup1 = (1) #tup1是整数不是元组
print(tup1)
tup2 = [1,]#加个逗号提示解释器这是元组符号不是括号运算符
print(tup2)

#空元组
tup3 = ()
print(tup3)

# 最后来看一个“可变的”tuple：

# >>> t = ('a', 'b', ['A', 'B'])
# >>> t[2][0] = 'X'
# >>> t[2][1] = 'Y'
# >>> t
# ('a', 'b', ['X', 'Y'])
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，
# 而是list的元素。tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
# 但指向的这个list本身是可变的！
# 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？
# 那就必须保证tuple的每一个元素本身也不能变。

#prac
lang = [
	['apple','google','MicroSoft'],
	['c','cpp','java','python'],
	['Ly','shengjiang','rbd','flei']
]
# 打印Apple:
print(lang[0][0])
# 打印Python:
print(lang[1][3])
# 打印shengjing:
print(lang[2][1])

testList = [1,2,3]
testList.insert(4,5)
print(testList)