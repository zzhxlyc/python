import time

#timestamp, but it is a float
print 'time.time()'
print time.time()

#mktime, return the struct_time to timestamp
print '\ntime.mktime()'
print time.mktime(time.localtime())

#ctime
print '\ntime.ctime()'
print time.ctime(time.time())   #Wed Jan 05 23:58:40 2011

#gmtime
print '\ntime.gmtime()'
print time.gmtime() #return time.struct_time (tm_year=2011, tm_mon=1, tm_mday=6, .....)
print time.gmtime(1000) #give a timestamp is ok

#localtime, depend on local timezone
print '\ntime.localtime()'
local = time.localtime()
print local     #return time.struct_time (tm_year=2011, tm_mon=1, tm_mday=6, .....)
print local[:]  #(2011,    1,    6,    0,    1,    44,    3,        6,        0) 
                #(year,    mon,  day,  hour, min,  sec,   weekday,  yearday,  DST)
                
#format time, strftime('pattern', struct_time)
print '\ntime.strftime()'
print time.strftime('Local time : %Y-%m-%d %H:%M:%S', time.localtime())
print time.strftime('The time : %Y-%m-%d %H:%M:%S', time.gmtime())

#parser time, strptime(timeString, 'pattern'), return a struct_time
print '\ntime.strptime()'
print time.strptime('2011-1-6 0:12:06', '%Y-%m-%d %H:%M:%S')

#get time pass
def time_cross(stru_time1, stru_time2):
    ret = time.mktime(stru_time2) - time.mktime(stru_time1)
    if ret < 0:
        ret = -ret
    year, month, day, hour, minute, second = time.gmtime()[0:6]
    year -= 1970    #the init time is 1970-1-1, so sub the year, month and day
    month -= 1
    day -= 1
    return {'year':year,'month':month,'day':day,'hour':hour,'minute':minute,'second':second}

print '\ntime_cross()'
time1 = time.strptime('2011-1-09 19:46:12', '%Y-%m-%d %H:%M:%S');
time2 = time.strptime('2011-1-10 19:46:12', '%Y-%m-%d %H:%M:%S');
print time_cross(time1, time2)

#thread sleep
time.sleep(1)