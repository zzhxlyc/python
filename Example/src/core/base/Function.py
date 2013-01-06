#coding=utf-8
'''
支持默认参数, 支持形参名与值绑定不按顺序输入
*arg3是元组类型变长参数
*arg4是字典类型变长参数
def func(arg1, arg2 = 1, *arg3, **arg4):
    pass
func(arg2 = 2, arg1 = 1)
func(1, 2, 3, 4, a = 5, b = 6)    #arg1=1, arg2=2, arg3=(3, 4), arg4={'a':5, 'b':6}

global关键字    : 全局参数
'''

#callable
callable(isinstance) # True 

#show the object's attribute in local symbol table
dir(str)

#unichr(num), turn the num to Unicode char
unichr(33333)

#zip(list1, list2, ...)    retuen a tuple list, which have all lists's same index elements
a = [1, 2, 3]
b = ['a', 'b', 'c']
zip(a, b) #[(1, 'a'), (2, 'b'), (3, 'c')]

#map(func, list)    make element in list done by func
'map',
map(ord, ['A', 'B', 'C'])     #[65, 66, 67]

#lambda
func = lambda a, b : a + b;     func(3, 4)

map((lambda x : x > 0), range(-5, 5))     #return the result whether x > 0, True or False

filter((lambda x : x > 0), range(-5, 5))  #return the x if x > 0

#意同MapReduce中的reduce的作用，将所有结果值用函数依次合并
reduce((lambda x, y : x + y), range(0, 5))#return the sum of list, same as ((((0+1)+2)+3)+4)
