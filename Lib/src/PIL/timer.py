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
        t, millSecond = divmod(usedTime, 1000)
        hour = t // 3600
        minute = (t - hour * 3600) // 60
        second = t - hour * 3600 - minute * 60
        return '%d hour %d minute %d second %d millSecond' %(hour, minute, second, millSecond)