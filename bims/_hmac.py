#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import hmac, hashlib, random

__author__ = 'Ly'

pwd = '88888888'
hmac_str = hmac.new('ly'.encode('utf-8'), pwd.encode('utf-8'), digestmod='MD5').hexdigest()
md5 = hashlib.md5()
md5.update(pwd.encode('utf-8'))
md5.update('ly'.encode('utf-8'))
md5_str = md5.hexdigest()
print(hmac_str, ',', md5_str)

#作业


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

