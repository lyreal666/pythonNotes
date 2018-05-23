#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from datetime import datetime, timedelta, timezone
import re

__author__ = 'LY'


'''
    test built_in_module datetime
    注意datetime是一个模块，我们用的是里面的datetime类
'''

# 获取当前系统时间
dt = datetime.now()
print(dt)
# 获取指定日期和时间的datetime对象
self_dt = datetime(1998, 1, 27, 0, 0, 0)
print(type(self_dt), self_dt)
# datetime转换为时间戳
tsp = dt.timestamp()
print(tsp)
# timestamp转datetime
print(datetime.fromtimestamp(tsp))
# utc时间
print(datetime.utcfromtimestamp(tsp))
# 字符串转date对象
dt_str = '1998,1,27 0,0,0'
dt_from_str = datetime.strptime(dt_str, '%Y,%m,%d %H,%M,%S')
print(dt_from_str)
# datetime获取格式时间字符串
time_str = datetime.strftime(datetime.now(), '%Y:%m:%d %H:%M:%S %a,%b')
print(time_str)
# datetime运算 使用timedelta计算时间差
dt1 = datetime(1998, 1, 27, 0, 0, 0)
dt2 = datetime(1997, 1, 27, 0, 00, 00)
dt3 = dt2 - dt1
print(type(dt3), dt3)
dt = datetime.now() + timedelta(days=365)
print(dt)
# 获取utc时间
utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
print()
# 获取北京时间
print(utc_time.astimezone(timezone(timedelta(hours=8))))


def to_timestamp(dt_str1, tz_str):
    dtm = datetime.strptime(dt_str1, '%Y-%m-%d %H:%M:%S')
    mr = re.match(r'^(UTC)([\+\-][0-1][0-9]|[\+\-][0-9])(:00)$', tz_str)
    dtm.replace(tzinfo=timezone(timedelta(hours=int(mr.group(2)))))
    tsp1 = dtm.timestamp()

    return tsp1


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')