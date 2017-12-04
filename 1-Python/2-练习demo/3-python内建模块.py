# 一、datetime模块
## 获取当前时间和日期
from datetime import datetime
now = datetime.now()
print(now)         # 2017-12-04 22:29:25.865744
print(type(now))   # <class 'datetime.datetime'>

## 获取制定日期和时间
from datetime import datetime
dt = datetime(2017,12,4,12,20)  # 用指定日期时间创建datetime
print(dt)            #2017-12-04 12:20:00

## datetime 转成 timestamp 
from datetime import datetime
dt = datetime(2017,12,04,12,20)  # 用指定日期时间创建datetime
dt.timestamp()                   # 把datetime转换成timestamp

## timestamp 转成 datetime
from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))   # 2015-04-19 12:20:00
## timestamp转UTC标准时区的时间
from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))   # 本地时间： 2015-04-19 12:20:00
print(datetime.utcfromtimestamp(t))# UTC时间： 2015-04-19 04:20:00

## str转换为datetime
from datetime import datetime
cday = datetime.strptime('2017-12-04 22:51:59','%Y-%m-%d %H:%M:%S')
print(cday)                        # 2017-12-04 22:51:59

## datetime转换为str
from datetime import datetime
now = datetime.now()
print(now.strftime('%a,%b,%d %H:%M'))# Mon,Dec,04 22:55

## datetime加减
from datetime import datetime,timedelta
now = datetime.now()
print(now)                                   # 2017-12-04 23:01:31.882059
print(now + timedelta(hours = 10))           # 2017-12-05 09:01:31.882059
print(now - timedelta(days = 1))             # 2017-12-03 23:01:31.882059
print(now + timedelta(days = 2,hours = 12))  # 2017-12-07 11:01:31.882059

## 本地时间转换成UTC时间
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.now()
print(now)                               # 2017-12-04 23:05:03.537432
dt = now.replace(tzinfo=tz_utc_8)        # 强制设置为UTC+8:00
print(dt)

## 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
from datetime import datetime, timedelta, timezone
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)                     # 2017-12-04 15:10:49.949725+00:00
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)                      # 2017-12-04 23:11:36.684443+08:00
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)                   # 2017-12-05 00:12:35.397543+09:00
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)                  # 2017-12-05 00:12:35.397543+09:00 
