import re

def openjson(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def query(path):
    URL = []
    IP = []
    data = openjson(path)
    #print(data)

    #提取域名
    url = re.findall(r'"rrname":.*",\n',data)
    for j in url:
        j=j.split('"')
        if j[3] not in URL:  #列表去重
            URL.append(j[3])

    #提取IP地址
    iplist = re.findall(r'\d+\.\d+\.\d+\.\d+', data)
    for i in iplist:
        if  i not in IP:  #列表去重
            IP.append(i)

    #域名写入文件
    URLfile = open(path[:-4]+'URL.txt', 'w', encoding='utf-8')
    for i in URL:
        URLfile.write(str(i)+'\n')
    URLfile.close()


    #IP 写入文件
    IPfile = open(path[:-4]+'IP地址.txt', 'w', encoding='utf-8')
    for i in IP:
        IPfile.write(str(i)+'\n')
    IPfile.close()




if __name__=="__main__":
    #filepath = input('请输入json文件路径：')
    filepath = "花椒直播域名.txt"
    #filepath = "360taojin.txt"
    data = query(filepath)




#print(a)
