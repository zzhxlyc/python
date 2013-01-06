#coding=utf-8
import math

def getOne(max):
    for i in range(max + 1): 
        yield i

gen = getOne(4)    #gen is a generator, like a iterator
print gen.next(), gen.next(), gen.next(), gen.next(), gen.next()

#for loop, if obj iterable call obj.next() until find StopIteration or use index visit obj[index]
for i in getOne(10):
    print i,
print
    
g = (x ** 2 for x in range(10) if x % 2)    #[]是列表解析, ()是 generator
print map(math.sqrt, g)

xrange  #是个immutable sequence

