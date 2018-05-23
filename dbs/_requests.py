#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'LY'

import requests

'''----------------------get-----------------------------'''
with requests.get('https://www.douban.com/') as fg:
    status = fg.status_code
    print('retcode:', status)
    print('reason', fg.reason)
    print('text:', fg.text)
    for k in fg.headers:
        print('%s: %s' % (k, fg.headers[k]))


attrs = {'q': 'python',
         'cat': '1001'
}
with requests.get('https://www.douban.com/', params=attrs) as fg:
    status = fg.status_code
    print('retcode:', status)
    print('reason', fg.reason)
    print('text:', fg.text)
    for k in fg.headers:
        print('%s: %s' % (k, fg.headers[k]))
    print(fg.encoding)
    print(fg.content)

str = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
with requests.get(str) as fj:
    json_obj = fj.json()
    print(json_obj)

headers = {
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
}
with requests.get('https://www.douban.com/', headers=headers) as fj:
   pass


'''---------------------post----------------------------'''
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
params = {'key': 'value'}
url = 'https://accounts.douban.com/login'
# 内部自动序列化为JSON
r = requests.post('https://accounts.douban.com/login', json=params)
upload_files = {'file': open('./imgs/code.jpg', 'rb')}
r = requests.post(url, files=upload_files)
print(r.headers)
print(r.headers['Content-Type'])
print(r.cookies['ts'])
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)
r = requests.get(url, timeout=2.5) # 2.5秒后超时