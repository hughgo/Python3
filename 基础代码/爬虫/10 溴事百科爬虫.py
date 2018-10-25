import urllib.request
import re

def jokeCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"

    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)

    HTML = response.read().decode("utf-8")

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'

    re_joke = re.compile(pat,re.S)
    divsList = re_joke.findall(HTML)
    # print(divsList)
    # print(len(divsList))
    dic = {}
    for div in divsList:
        re_u = re.compile(r"<h2>(.*?)</h2>",re.S)
        username = re_u.findall(div)
        username = username[0]

        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duzi = re_d.findall(div)
        duzi = duzi[0]
        print(duzi)

        dic[username]=duzi
    return dic

    # with open(r"C:\fle\file1.html","wb") as f:
    #     f.write(HTML)


url= "https://www.qiushibaike.com/text/page/2/"
info = jokeCrawler(url)

for k,v in info.items():
    print(k,v)
