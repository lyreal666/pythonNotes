#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import struct
import base64

__author__ = 'Ly'

'''
    使用 struct 模块获取二进制字节字符
    BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

    两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
    一个4字节整数：表示位图大小；
    一个4字节整数：保留位，始终为0；
    一个4字节整数：实际图像的偏移量；
    一个4字节整数：Header的字节数；
    一个4字节整数：图像宽度；
    一个4字节整数：图像高度；
    一个2字节整数：始终为1；
    一个2字节整数：颜色数。
'''

bin_bytes = struct.pack('>I', 1234)
print(bin_bytes)

int_data = struct.unpack('>I', bin_bytes)
print(int_data)

# 作业


def bmp_info(data):

    rs = struct.unpack('<cc', data[0:2])
    fm = rs[0] + rs[1]
    print(fm)
    if fm == b'BM' or b'BA':
        width = struct.unpack('<I', data[18:22])[0]
        height = struct.unpack('<I', data[22:26])[0]
        color = struct.unpack('<H', data[28:30])[0]
        print(width, height, color)
        return {
            'width': width,
            'height': height,
            'color': color
        }
    else:
        return None


bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABA'
                            'BAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//'
                            'f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f'
                            '/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB'
                            '8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AH'
                            'wAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfA'
                            'B8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3/'
                            '/f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8'
                            'AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfA'
                            'B8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38'
                            'AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB'
                            '8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3/'
                            '/f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB'
                            '8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwA'
                            'fAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AH'
                            'wAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8'
                            '/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f'
                            '/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//'
                            '3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')