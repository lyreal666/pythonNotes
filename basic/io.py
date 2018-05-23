#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'test io'
__author__ = 'LY'

#---------------read file-------------------#
try:
	with open("./testio.txt",'w',encoding='utf-8') as fw:
		fw.write('奥古斯都')
		fw.flush()

	with open('./testio.txt','r',encoding='utf-8') as fr:
		print(fr.read())
except IOError as e:
	print("ioexception")
finally:
	pass


import os,time

def dir_l(path = '.'):
	try:
		flist = [os.path.join(path,d) for d in os.listdir(path)]
	except FileNotFoundError as e:
		print("找不到文件，请检查路径!")
		return None

	print('路径 ' + os.path.abspath(path) + '下的文件列表信息:')
	print('%-12s\t%5s\t%6s\t%10s\tfilename' % ('finaldate','time','type','size'))
	for f in flist:
		try:
			mt = os.path.getmtime(f)
			mdate = time.strftime("%Y-%m-%d",time.localtime(mt))
			mtime = time.strftime("%H:%M",time.localtime(mt))
			ftype = '<DIR>' if os.path.isdir(f) else '<FILE>'
			fsize = os.path.getsize(f)
		except FileNotFoundError as e:
			mdate = ''
			mtime = ''
			ftype = ''
			fsize = 0

		print('%-12s\t%5s\t%6s\t%10s\t%s' % (mdate,mtime,ftype,str(fsize),f))

if __name__ == '__main__':
	dir_l('D:')

def findFile(name,d = '.'):
	if not isinstance(name,str) or not os.path.exists(d):
		print('类型不正确或路径有问题')
		return None

	flist = os.listdir(d)
	for f in flist:
		path = os.path.join(d,f)
		if os.path.isdir(path):
			findFile(name,path)
		else:
			if f == name:
				print(path)

if __name__ == '__main__':
	findFile('io.py','F:\codingSpace')