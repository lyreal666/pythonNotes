#!/usr/bin/env python3
# -*- coding:utf-8 *-*

__author__ = 'LY'

'''-----------test pickle------------'''
import pickle

d = {'name': 'ly', 'age': 20}
bs = pickle.dumps(d)
print(bs)

with open('fw.txt', 'wb') as fw:
    pickle.dump(d, fw)

dl = pickle.loads(bs)
print(dl)

with open('fw.txt', 'rb') as fr:
    df = pickle.load(fr)
    print(df)

'''------------------test json-------------------'''
import json

d2 = {'name': '紫罗兰', 'sex': 'woman'}
json_str = json.dumps(d2, ensure_ascii=False)
print(json_str)

d3 = json.loads(json_str)
print(d3)

with open('json_str.txt', 'w') as fj:
    json.dump(d2, fj, ensure_ascii=False)

with open('json_str.txt', 'r') as fjr:
    json_str2 = json.load(fjr)
    print(json_str2)

'''-----------------------higher json skill---------------------'''


class Person(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def person_to_dict(person):
    return {'name': person.name, 'age': person.age, 'score': person.score}


p = Person('LiMing', 18, 100)
json_str3 = json.dumps(p, default=person_to_dict)


def dict_to_person(d):
    return Person(d['name'], d['age'], d['score'])


p1 = json.loads(json_str3, object_hook=dict_to_person)
print(p1)

p2 = Person('LanLan', 20, 89)
json.dumps(p2, default=lambda per: per.__dict__)