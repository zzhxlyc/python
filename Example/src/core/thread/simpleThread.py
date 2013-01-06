import thread, threading, time

printLock = thread.allocate_lock()  #it is a mutex
printLock2 = threading.Lock()       #the same

def displayTime(interval):
    while True:
        printLock.acquire()     #acquire() block the thread
        print 'Time is', time.ctime(time.time())
        time.sleep(interval)
        printLock.release()
        
thread.start_new_thread(displayTime, (1,))

while True:
    printLock.acquire()
    print 'hello world'
    time.sleep(1)
    printLock.release()
    
#if the main thread is over, all thread over