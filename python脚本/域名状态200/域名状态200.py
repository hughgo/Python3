import requests
import threading
import queue

q = queue.Queue() # Queue产生一个队列，有3种类型队列 默认用 FIFO队列
threading_num = 50 # 开启50个线程

# 打开字典文件，
with open("../json提取IP域名/花椒直播域名URL.txt" , "r") as f:
    filedata = f.readlines()
    q.put(filedata)
    f.close() #将line传入到队列 q 中

def run():
    while not q.empty():
        filedata = q.get()
        for i in filedata:
            url = 'http://'+str(i).replace("\n",'')
            #print(url)
            try:
                data = requests.get(url,timeout=0.1)
                num = data.status_code
                if num ==200:
                    print(url)
            except:
                #print('无法访问此网站')
                pass
        #f.close()

if __name__ =="__main__":
    print('测试开始！')
    for i in range(threading_num):
        t = threading.Thread(target=run)
        t.start()
        t.join()
    print('测试结束！')


