from multiprocessing import Process
import os,time
class qianxiao996(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name=name
    def run(self):
        print('子进程(%s-%s)启i动'%(self.name,os.getpd()))
        time.sleep(3)
        print('子进程(%s-%s)结束' % (self.name, os.getpid()))