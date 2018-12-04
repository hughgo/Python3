#数字字典生成器  by qianxiao996
#博客地址：https://blog.csdn.net/qq_36374896

#此程序输入开始结束和位数即可在程序所在目录下生成字典
#只支持数字生成

start = int(input("请输入开始的数值："))
end = int(input("请输入结束的数值："))
num = int(input("请输入生成的位数："))
path = str(start)+"到"+str(end)+"的"+str(num)+"位数字典.txt"#输出的字典名

for i in range(start,end+1):   # 生成从start到end的字典
    s = str(i).zfill(num)         #生成六位数的字典
    with open(path,"a",encoding='utf-8') as f:  #打开文件
        f.write(str(s) + "\n")    #写入文件
        print(str(s))
        f.close()



