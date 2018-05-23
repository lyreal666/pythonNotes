#!usr/bin/env/ python3
# -*- coding: utf-8 -*-

age = int(input("input your name："))

if age < 12 :
	print("a child")
elif age >= 12 and age < 18 :
	print("a teenager")
elif age >= 18 and age < 40 :
	print("a adult")
else :
	print("old")

#斐波那契数列中求第二十个20
febo = [1,1]
p = 2
while p <= 19 :
	febo.append(0)
	febo[p] = febo[p - 1] + febo[p - 2]
print(febo[19])

res = 0
for e in range(101) :
	res += e
print(res)