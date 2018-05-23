#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"higher oop"

__author__ = "LY"

#----------------------------使用注解写bean-----------------------------------#
class Screen(object):
    @property
    def width(self):
    	return self.__width

    @width.setter
    def width(self,newWidth):
    	if not isinstance(newWidth,(int,float)):
    		raise TypeError("参数类型错误")
    	else:
    		self.__width = newWidth

    @property
    def height(self):
    	return self.__high

    @height.setter
    def height(self,newHigh):
    	if not isinstance(newHigh,(int,float)):
    		raise TypeError("参数类型错误")
    	else:
    		self.__high = newHigh

    @property
    def resolution(self):
    	return self.__high * self.__width
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

# Screen().width = 10
class Test:
	pass

print(dir(Test()))

from enum import Enum , unique

@unique
class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')



Season = Enum('Season',('Spring','summer','autumn','winter'))

for s,v in Season.__members__.items():
	print(s,v)

print(type(Season.Spring))
print(Season(2))
print(Season['autumn'])


def def_run(self):
	print("run")

Animal = type("Animal",(object,),dict(run = def_run))

ani = Animal()

ani.run()

print(__name__)
