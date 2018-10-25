import hashlib

h1 = hashlib.md5()
f0 = open("C:/Users/Master/Desktop/Files/pwd/passwordtop1000md5.txt", 'a+')
f = open("C:/Users/Master/Desktop/Files/pwd/TOP1000.txt", 'r')
line = f.readline()

while line:


    line.strip('\n')
    h1.update(line.encode("UTF-8"))
    passwordmd5 = line + h1.hexdigest() + "\n"
    f0.write(passwordmd5)
    line = f.readline()


f.close()
f0.close()
