#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

import psutil

# 逻辑核心和非逻辑核心不一样代表多出来的是超频
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

# cpu工具
print(psutil.Process)
print(psutil.cpu_stats())
# for t in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.cpu_times())

# 内存工具
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 磁盘工具
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())

# 网络工具
print('addr: ', psutil.net_if_addrs())
print('status: ', psutil.net_if_stats())
print(psutil.net_io_counters())
print(psutil.net_connections())

# 进程工具
print(psutil.test())
print(psutil.pids())
p = psutil.Process(1216)
print(p.cpu_percent(interval=1))
print(p.cwd())
p.terminate()
print(psutil.test())
