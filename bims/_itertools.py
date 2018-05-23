#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import itertools

__author__ = 'Ly'


'''-----------------无限迭代器----------------------'''
iter0 = itertools.count(1)
# for i in iter0:
#     print(i)
iter1 = itertools.cycle('abc')
# for i in iter1:
#     print(i)
iter2 = itertools.repeat('abc')


'''-----------------迭代器操作函数----------------------'''
#
iter3 = itertools.takewhile(lambda x: x < 10, iter0)
# for i in iter3:
#     print(i)
iter4 = itertools.chain('xyz', 'abc')
# for i in iter4:
#     print(i)
iter5 = itertools.groupby('aaaAAbbbccccdddd', lambda x: x.upper())
for i in iter5:
    print(i)


# 作业
# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     oddlist = itertools.count(1, step=2)
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     oddlist = itertools.takewhile(lambda x: x <= 2 * N - 1, oddlist)
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     flag = 1
#     lis = []
#     oddlist = [4 / e for e in oddlist]
#     for e in oddlist:
#         e = flag * e
#         flag = -flag
#         lis.append(e)
#     # step 4: 求和:
#     res = 0
#     for e in lis:
#         res += e
#     return res
# 网友答案
def pi(N):
    oddlist = itertools.count(1, 2)
    preN = itertools.takewhile(lambda x: x <= 2 * N -1, oddlist)
    zf = itertools.cycle([+4, -4])

    return sum([next(zf) / next(preN) for t in range(N)])


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')