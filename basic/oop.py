#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'test oop'

__author__ = "LY"

class Student(object):
	def __init__(self, name,gender):
		self.__name = name
		self.__gender = gender

	def set_gender(self,gender) :
		self.__gender = gender

	def get_gender(self) :
		return self.__gender


#print(__name__)

if __name__ == '__main__' :
	# 测试:
	bart = Student('Bart', 'male')
	if bart.get_gender() != 'male':
	    print('测试失败!')
	else:
	    bart.set_gender('female')
	    if bart.get_gender() != 'female':
	        print('测试失败!')
	    else:
	        print('测试成功!')


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

class TestObj(object):
	count = 0
	def __init__(self):
		TestObj.count += 1
		
t1 = TestObj()
t2 = TestObj()
t3 = TestObj()
print(t3.count)