
'''
此模块下的类具有同步及阻塞措施
Queue(maxsize=0)           FIFO队列
LifoQueue(maxsize=0)       栈型队列
PriorityQueue(maxsize=0)   使用heapq保持

Queue.Empty    空时候get的异常
Queue.Full     满时候put的异常

Queue.qsize()
Queue.empty() 
Queue.full()
Queue.put(item[, block[, timeout]])     #当block = True, timeout才有用
Queue.get([block[, timeout]]) 
'''
