#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def comp(x,y) :
	if x < y :
		return True
	else :
		return False

from collections import Iterator,Iterable
def getBiggest(cmparator,*ls) :
	if isinstance(ls,Iterable) :
		if not len(ls) == 0 :
			biggest = ls[0]
			for e in ls :
				if cmparator(biggest,e) :
					biggest = e

			return biggest
		
	return None

tlis = [1,2,3,4]
print(getBiggest(comp,*tlis))
		
L = list(filter(lambda n : n % 2 == 1,range(1,20)))
	

import time, functools

def metric(fn) :
	@functools.wraps(fn)
	def wrapper(*argc,**kw):
		tbeg = time.time()
		res = fn(*argc,*kw)
		tend = time.time()
		print("%s execute in  %s seconds" % (fn.__name__,tend - tbeg))

		return res
	return wrapper
    

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')