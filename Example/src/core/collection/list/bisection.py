#coding=utf-8
import bisect

'''
利用二分法维持sorted的list
bisect(list, item[, lo[, hi]]) list为sorted的, lo和hi为list的边界, 默认为整个list 
'''

aray = [1, 2, 3, 4, 5]

index = bisect.bisect_left(aray, 3)     #遇到相等的item返回左边的index
index = bisect.bisect_right(aray, 3)    #遇到相等的item返回右边的index

#通过bisect得到index后，调用list.insert()实现
bisect.insort_left(aray, 2.5)   #遇到相等的item插入左边的index
bisect.insort_right(aray, 3)    #遇到相等的item插入右边的index

