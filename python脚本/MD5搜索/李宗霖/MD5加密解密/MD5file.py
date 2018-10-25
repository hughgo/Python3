import hashlib
filename ='1.txt'
cc= input('是否要查询:')
if cc == '1' :
    str=input('输入要查询的MD5:')
with open(filename) as f:
    lines = f.readlines()
    f.close()
for line in lines:
    m = hashlib.md5()
    m.update(line.encode("utf-8"))
    line_md5 = m.hexdigest()
  #  print(line_md5)
  #  print(line)
    with open('2.txt','a') as f:
        f.write(line_md5)
        f.write("\n")
        f.close()
print("完成")
if cc == '1':
    with open(filename) as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        m = hashlib.md5()
        m.update(line.encode("utf-8"))
        line_md5 = m.hexdigest()
        if cc == '1':
            if str == line_md5:
                print("查找的是")
                print(line)
                cc = 0
