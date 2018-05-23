import pdb

'several debug methods'

__author__ = 'LY'

li = [1,2,3,4,5,6,7,8,9,10]
index = 10
# #---------------------使用print()函数-------------------------#
# print(index)

# #---------------------使用assert断言-------------------------#
# assert index < 10,'outOfBound error'

# #---------------------使用logging-------------------------#
# #logging level 有debug,info,warnning,error
# import logging
# logging.basicConfig(level=logging.DEBUG)

# logging.debug("%d" % index)

#---------------------使用pdb single debug-------------------------#



pdb.set_trace()
#print(li[10])
print('dd')
pdb.set_trace()
print('END')