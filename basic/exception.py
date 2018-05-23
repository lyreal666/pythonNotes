#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce
import logging

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)

    try:
    	res = reduce(lambda acc, x: acc + x, ns)
    except BaseException as e:
    	print("有异常")
    	res = 0
    	logging.exception(e)
    finally:
    	print("....")

    return res

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
    raise ZeroDivisionError("0除错误")
    raise ValueError("测试。。。。")

main()


