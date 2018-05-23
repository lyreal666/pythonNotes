#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import namedtuple, Counter, deque, defaultdict, OrderedDict

__author__ = 'LY'

'''
    测试集合模块
'''

'''------------------------具名元组namedtuple-----------------------------'''
Student = namedtuple('Student', ('name', 'age', 'height'))
stu1 = Student('Ly', '20', '170')
print(type(stu1), stu1)
print(isinstance(stu1, tuple))


'''----------------------计数器----------------------------'''
counter1 = Counter()
str1 = 'abbaaacddfffeeejsdhkvmkadfsaldwpwdlsxhjvasbqwdgg'
for c in str1:
    counter1[c] += 1
print(counter1)
print(counter1['a'])


'''--------------------deque 双向队列-----------------------------'''
# 当队列用
deq = deque([1, 2, 3, 4, 5])
print(deq)
deq.append(6)
for e in range(6):
    print(deq.popleft())

# 当堆栈用
stk = deque()
for s in range(6):
    stk.append(s)
for s in range(6):
    print(stk.pop())

stk.appendleft(-1)


'''----------------------defaultdict 带默认值的dict--------------------------'''
dd = defaultdict(lambda: '米有')
dd['a'] = 'Alice'
print(dd['a'])
print(dd['b'])
print(isinstance(dd, dict))
print('a' in 'abc')


'''---------------------OrderedDict 输出有序------------------------------'''
d = {'a': 'alice', 'b': 'bob', 'c': 'carry', 'd': 'david'}
for t in range(100):
    print(list(d.keys()))

od = OrderedDict()
od['a'] = 'alice'
od['b'] = 'bob'
od['c'] = 'carry'
od['a'] = 'gg'
print(list(od.keys()))


class FIFOdict(OrderedDict):
    def __init__(self,capacity):
        super(FIFOdict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        if key not in self and len(self) == self.capacity:
            self.popitem(last=False)
        if key in self:
            del self[key]

        OrderedDict.__setitem__(self, key, value)
