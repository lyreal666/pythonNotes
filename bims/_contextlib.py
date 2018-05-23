#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from contextlib import contextmanager, closing

'''
    实现了__enter__和__exit__函数对象可以使用with语句
    执行with语句块之前执行__enter__
    with语句块内容执行完后执行__exit__
    
    使用@contextmanager管理上下文
'''

__author__ = 'LY'


with open('test.txt', 'w') as fw:
    fw.write('测试上下文库')


class Querry(object):
    def __init__(self, name):
        print('create a Querry obj')
        self.name = name

    def __enter__(self):
        print('do something before querry obj work...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close the resource....')


with Querry('Ly') as q:
    print('work...............')


'''------------------使用contextmanager decorator----------------------'''


class Context(object):
    def __init__(self, name):
        print('create a Querry obj')
        self.name = name


@contextmanager
def create_context(name):
    print('do something before querry obj work...')
    yield Context(name)
    print('close the resource....')


with create_context('mary') as c:
    pass


class Auto_Close(object):
    def __init__(self, name):
        print('create a Querry obj')
        self.name = name

    def close(self):
        print('close the resource....')


with closing(Auto_Close()) as a:
    pass
