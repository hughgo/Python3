import os
path = os.path.abspath('字典.txt')
for i in range(0,9999):
    s = str(i).zfill(6)
    with open(path,"a+") as f:
        f.write(str(s) + "\n")
        f.close()
