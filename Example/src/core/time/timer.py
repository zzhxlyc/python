import time

class Timer():
    
    def begin(self):
        self.begin = time.time() * 1000
        
    def end(self):
        self.end = time.time() * 1000
        
    def getTime(self):
        return self.end - self.begin
    
    def getTimeString(self):
        usedTime = long(self.getTime())
        allInSeconds, millSecond = divmod(usedTime, 1000)
        hour = allInSeconds // 3600
        minute = (allInSeconds - hour * 3600) // 60
        second = allInSeconds - hour * 3600 - minute * 60
        return '%d hour %d minute %d second %d millSecond' % (hour, minute, second, millSecond)
