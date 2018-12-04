import cmath
num = int(input('请输入一个数字:'))
#num_sqrt = num*0.5
num_sqrt = cmath.sqrt(num)
print('{0}的平方根为{1} ' .format(num,num_sqrt) )