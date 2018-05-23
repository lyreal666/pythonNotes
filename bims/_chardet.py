#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

import chardet

data1 = '我是utf-8字符'.encode('utf-8')
print(chardet.detect(data1))

data2 = '我是gb16030'.encode('gbk')
print(chardet.detect(data2))

print(chardet.detect(b'abcdef'))