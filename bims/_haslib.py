#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib

__author__ = 'LY'

'''
    测试摘要算法md5, sha1
'''

md5 = hashlib.md5()
md5.update('ytjc++1314'.encode('utf-8'))
md5.update('ytjjava1314'.encode('utf-8'))
md5_str = md5.hexdigest()
print(type(md5_str), len(md5_str))

sha1 = hashlib.sha1()
sha1.update('12345678'.encode('utf-8'))
sha1.update('00000000'.encode('utf-8'))
sha1_str = sha1.hexdigest()
print(sha1_str, len(sha1_str))


# 作业
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    _md5 = hashlib.md5()
    _md5.update(password.encode('utf-8'))
    hex_password = _md5.hexdigest()
    if db[user] == hex_password:
        return True
    else:
        return False


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')