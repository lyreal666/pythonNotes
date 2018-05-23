#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'简易ORM框架python实现'


class Field(object):
	def __init__(self,name,column_type):
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return 'Field object(%r,%r)' %  (self.name,self.column_type)

class IntegerField(Field):
	def __init__(self,name):
		super.__init__(name,'bigint')

class StringField(Field):
	def __init__(self,name):
		super.__init__(name,"verchar(200")

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name == 'Model':
			return type.__(cls,name,bases,attrs)
		else:
			mappings = dict()

			for k,v in attrs.items():
				if isinstance(v,(IntegerField,StringField)):
					mapping[k] = v

			for k in mappings.keys()：
				attrs[k].pop()

			attrs["__mapping__"] = mappings
			attrs['__tablename__'] = name

			return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass = ModelMetaclass):
	def __init(self):
		pass

	def 

class User(Model):
	id = IntegerField('id')
	name = StringFiled('name')
	email = SringField('email')
	password = StringField('password')
