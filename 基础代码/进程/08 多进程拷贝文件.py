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


if __name__=='__main__':
#读取path下的文件
    filesList = os.listdir(path)

    start = time.time()
    pp=Pool(4)
    for filename in filesList:
        pp.apply_async(copyFile,args=(os.path.join(path,filename),os.path.join(toPath,filename)))
    pp.close()
    pp.join()
    end = time.time()
    print('总耗时:%0.2f'% (end-start))