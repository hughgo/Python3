def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

num1 = int(input('请输入第一个数字:'))
num2 = int(input('请输入第二个数字:'))

print('选择运算：')
print('1.相加')
print('2.相减')
print('3.相乘')
print('4.相除')
choice = int(input('请输入你的选择：'))

if choice==1:
    print(num1,'+',num2,'=',add(num1,num2))
if choice==2:
    print(num1,'-',num2,'=',subtract(num1,num2))
if choice ==3:
    print(num1, '*', num2, '=', multiply(num1, num2))
if choice==4:
    print(num1,'/',num2,'=',divide(num1,num2))