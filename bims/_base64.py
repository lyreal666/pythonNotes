#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64

__author__ = 'LY'

'''
    测试base64
'''

b64_str = base64.b64encode(b'abc')
print(b64_str)
print(base64.b64decode(b64_str))

# url_safe 把+,=转换为别的字符
bin_str = base64.b64decode(b'++//')
print(bin_str)
safe_b64_str = base64.urlsafe_b64encode(b'\xfb\xef\xff')
print(safe_b64_str)

# 作业


def safe_base64_decode(s):
    left = 4 - len(s) % 4
    if left == 4:
        return base64.urlsafe_b64decode(s)
    else:
        for t in range(left):
            s += b'='
        return base64.urlsafe_b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')


