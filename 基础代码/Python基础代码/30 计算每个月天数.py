import calendar
#输出第一天是星期几，和每个月天数
monthRange = calendar.monthrange(2016, 9)
print(monthRange)

#只输出每个月的天数
print(calendar.mdays[9])
