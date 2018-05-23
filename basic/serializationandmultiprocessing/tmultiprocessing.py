#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import time
import random
import subprocess
from multiprocessing import Process, Pool, Queue

__author__ = 'LY'

'''
    测试多进程
'''
'''-------unix/linux/mac 下的fork()系统api调用------'''


# # os.getpid获取当前进程id
# print('process %s is start...' % os.getpid())
# # fork调用后当前进程被复制，通过返回值确定是父进程还是子进程
# pid = os.fork()
# # 子进程返回0,父进程返回子进程id
# if pid == 0:
#     print("I'm child process (%s)" % os.getpid())
# else:
#     print("I (%s) just created a child process (%s)" % (os.getpid(), pid))

'''----------------跨平台多进程模块 multiprocessing-----------------'''

# 定义子进程执行代码


def run_child(name):
    print('run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process (%s) starts' % os.getppid())
    p = Process(target=run_child, args=('test',))
    print('child process test will start....')
    p.start()
    p.join()
    print('Child process end..')

'''----------------------使用进程池Pool管理大量子进程-----------------'''


def long_time_task(name):
    print('Run the task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print('Task %s run %s s' % (name, end - start))


if __name__ == '__main__':
    print('Parent process (%s) starts...' % os.getpid())
    pool = Pool(4)
    for proc in range(5):
        pool.apply_async(long_time_task, args=(proc,))

    print('all child process has ran....')
    pool.close()
    pool.join()
    print('all child process has done....')


'''-------------------子进程----------------------'''
if __name__ == '__main__':
    print('Run the command ==> python -V')
    r = subprocess.call(['python', '-V'])
    print('Exit code is %s' % r)
# 与子进程通信
if __name__ == '__main__':
    print('Run the command $ nslookup')
    sp = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = sp.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8',errors='ignore'))
    print('Exit code is %s' % sp.returncode)


'''----------------进程之间的通信------------------'''
# 使用Queue


def run_write(q):
    print('write process starts.....')
    for w in ['A', 'B', 'C', 'D', 'E']:
        print('put value %s to queue....' % w)
        q.put(w)
        time.sleep(random.random())


def run_read(q):
    print('read process starts.....')
    while True:
        w = q.get()
        print('get the value %s from queue' % w)


if __name__ == '__main__':
    print('主进程(%s) s tart...' % os.getpid())
    queue = Queue()
    pw = Process(target=run_write,args=(queue,))
    pr = Process(target=run_read,args=(queue,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
