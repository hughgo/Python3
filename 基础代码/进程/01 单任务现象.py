from time import  sleep
def run():
    while True:
        print('sunck is man')
        sleep(1.2)
if __name__=="__main__":
    while True:
        print("sun is a man")
        sleep(1)
    #不会执行到run 只有上面的循环结束才会执行
    run()