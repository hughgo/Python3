#coding-UTF-8
import urllib.request
import re
import os


def imageCrawler(url,toPath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)

    HtmlStr = response.read().decode("utf-8")



    #print (HtmlStr)
    # with open(r"C:\Users\admin\Desktop\360学习\爬虫\image\1.html","wb")as f:
    #   f.write(HtmlStr)
    pat = r'<img src="//(.*?)"/>'


    re_image = re.compile(pat,re.S)
    imagesList=re_image.findall(HtmlStr)
    #print (imagesList)
    num=1

    for imagesURL in imagesList:
        path = os.path.join(toPath,str(num)+".jpg")
        num +=1
        #把图片下载到本地存储
        urllib.request.urlretrieve("http://"+imagesURL,filename=path)
    #print(imagesList)
    #print(len(imagesList))
    #print(imagesList[0])





url = "http://search.yhd.com/c0-0/k%25E7%2594%2598%25E7%2594%259C%25E6%25B0%25B4%25E6%259E%259C/"

toPath = r"C:\Users\admin\Desktop\360学习\爬虫\image"

imageCrawler(url,toPath)