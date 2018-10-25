import threading
import time
#控制几个线程执行
bar = threading.Barrier(3)

def run():
    print("%s-start"%(threading.current_thread().name))
    time.sleep(1)
    bar.wait()
    print("%s-end"%(threading.current_thread().name))

if __name__=="__main__":
    for i in range(5):
        threading.Thread(target=run).start()
