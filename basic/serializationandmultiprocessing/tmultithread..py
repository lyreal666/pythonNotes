#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time
import random
import multiprocessing

__author__ = 'Ly'

'''
    test multi_thread
'''

'''-----------thread----------------------'''


def loop():
    print('Thread (%s) starts....' % threading.current_thread().name)
    for n in range(5):
        print('Thread (%s) ==> %d' % (threading.current_thread().name, n))
        time.sleep(random.random())
    print('Thread (%s) end...' % threading.current_thread().name)


if __name__ == '__main__':
    print('Thread (%s) starts....' % threading.current_thread().name)

    t = threading.Thread(target=loop, name='loopthread')
    t.start()
    t.join()

    print('Thread (%s) end...' % threading.current_thread().name)


'''-----------------------lock----------------------------'''
balance = 0
balance1 = 0


def change_op(count):
    global balance
    balance = balance + count
    balance = balance - count


def run_thread(count):
    print('Thread (%s) starts....' % threading.current_thread().name)
    for t in range(1000000):
        change_op(count)
    print('Thread (%s) end...' % threading.current_thread().name)


def run_thread_lock(count):
    print('Thread (%s) starts....' % threading.current_thread().name)
    lock = threading.Lock()
    for t in range(1000000):
        lock.acquire()
        try:
            change_op(count)
        finally:
            lock.release()
    print('Thread (%s) end...' % threading.current_thread().name)


if __name__ == '__main__':
    print('Thread (%s) starts....' % threading.current_thread().name)
    t1 = threading.Thread(target=run_thread, args=(5,), name='sale1')
    t2 = threading.Thread(target=run_thread, args=(8,), name='sale2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(balance)
    print('Thread (%s) end...' % threading.current_thread().name)

if __name__ == '__main__':
    print('Thread (%s) starts....' % threading.current_thread().name)
    t3 = threading.Thread(target=run_thread, args=(5,), name='sale3')
    t4 = threading.Thread(target=run_thread, args=(8,), name='sale4')

    t3.start()
    t4.start()

    t3.join()
    t4.join()

    print(balance1)
    print('Thread (%s) end...' % threading.current_thread().name)

print(multiprocessing.cpu_count())


'''----------------------thread local--------------------------'''
thread_local = threading.local()


def process_student():
    stu = thread_local.stu
    print('student %s in thread %s' % (stu, threading.current_thread().name))


def process_thread(name):
    thread_local.stu = name
    process_student()


sth1 = threading.Thread(target=process_thread, args=('AiLi',))
sth2 = threading.Thread(target=process_thread, args=('LY',))

sth1.start()
sth2.start()

sth1.join()
sth2.join()
