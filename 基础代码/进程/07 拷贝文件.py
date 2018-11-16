import  os
from multiprocessing import Pool
import time



def copyFile(rPath,wPath):
    fr = open(rPath,'rb')
    fw=open(wPath,'wb')
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path=r'C:\Users\admin\Desktop\新建文件夹'
toPath=r'C:\Users\admin\Desktop\爱按'

#读取path下的文件
filesList = os.listdir(path)

#启动for循环处理每个文件
start = time.time()
for fileName in filesList:
    copyFile(os.path.join(path,fileName),os.path.join(toPath,fileName))
end= time.time()
print('总耗时:%0.2f'% (end-start))