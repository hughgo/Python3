year = int(input("请输入一个年份："))
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print('这是一个闰年')
else:
    print('这不是一个闰年')