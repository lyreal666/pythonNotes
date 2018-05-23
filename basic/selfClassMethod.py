#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"一些用于定制类的方法"

__author__ = "Ly"


class TestObject(object):
	__slots__ = ("y","z")
	def __init__(self,x):
		self.x = x

	def __str__(self):
		print("TestObject object(x:%r)" % self.x)

	def __repr__(self):
		self.__str__()

	def __getitem__(self):
		pass

	def __len__(self):
		pass

	def __getattr__(self):
		pass

	def __call__(self):
		pass

	def __iter__(self):
		pass

	def __next__(self):
		pass

	def __add__(seld):
		pass

	def __mul__(self):
		pass


