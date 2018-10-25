import urllib.request
import ssl
import re
import os

def writeFile1Bytes(htmlBytes,toPath):
    with open(toPath,"wb") as f:
        f.write(htmlBytes)
def writeFile1Str(htmlBytes,toPath):
    with open(toPath,"wb") as f:
        f.write(htmlBytes)

def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read()

def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    # writeFile1Bytes(htmlBytes,r"C:\Users\admin\Desktop\360学习\爬虫\image\qq1.html")
    # writeFile1Str(htmlBytes,r"C:\Users\admin\Desktop\360学习\爬虫\image\qq2.txt")
    htmlStr = str(htmlBytes)

    pat = r"[1-9]\d{4,9}"
    re_qq= re.compile(pat)
    qqsList = re_qq.findall(htmlStr)


    qqsList = list(set(qqsList))
    print(qqsList)
    print(len(qqsList))


url="http://tieba.baidu.com/p/5471533241?traceid="
toPath=r"C:\Users\admin\Desktop\360学习\爬虫\image\qq.txt"
qqCrawler(url,toPath)