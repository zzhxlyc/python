import time
from datetime import date,datetime

#Class date
d = date(2010,1,16)
d = date.today()
d = date.fromtimestamp(time.time())
d = d.replace(year = 2012)
print d, d.weekday()
print d.strftime('%Y-%m-%d %H:%M:%S')

#Class time

#Class datetime
print datetime.today(), datetime.now()
dt = datetime.now()
dt.t