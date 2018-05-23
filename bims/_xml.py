#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from xml.parsers.expat import ParserCreate
from _datetime import datetime
from urllib import request

__author__ = 'Ly'

#作业
# input('请输入城市代号:')


class MyParser(object):
    def __init__(self):
        self.data = {
        'city': '1',
        'forecast': []
        }

    def start_element(self, name, attrs):
        if name == 'yweather:location' and 'city' in attrs:
            self.data['city'] = attrs['city']

        if name == 'yweather:forecast':
            self.data['forecast'].append({
                'date': datetime.strptime(attrs['date'], '%d %b %Y').strftime(
                    '%Y-%m-%d'
                ),
                'high': attrs['high'],
                'low': attrs['low']
            })

    def char_data(self, text):
        pass

    def end_element(self, name):
        pass


def parseXml(xml_str):
    myparser = ParserCreate()
    handle = MyParser()
    myparser.StartElementHandler = handle.start_element
    myparser.EndElementHandler = handle.end_element
    myparser.CharacterDataHandler = handle.char_data
    myparser.Parse(xml_str)
    return handle.data


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print(result)
print('ok')