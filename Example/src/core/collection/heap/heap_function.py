#coding=utf-8
import heapq

'''
默认为最小堆
'''

heap = [2]
heapq.heapify(heap)   #in linear time

heapq.heappush(heap, 1)
top = heapq.heappop(heap)        #抛出顶端最小值, 无元素抛IndexError  
top = heapq.heappushpop(heap, 2) #先push再pop出top值
top = heapq.heapreplace(heap, 3) #先pop出top值再push, 效率比heappop()再heappop()高

lt = heapq.nlargest(5, heap)     #heapq.nlargest(n, iterable[, key]) , Nlogn
lt = heapq.nsmallest(5, heap)    #heapq.nsmallest(n, iterable[, key]) 