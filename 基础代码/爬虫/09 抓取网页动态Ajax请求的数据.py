import  urllib.request
import ssl
import json

def ajaxCrawler(url):
    headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",

    }
    req = urllib.request.Request(url,headers)

    #使用ssl创建未验证的ssl
    context =  ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)

    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return  jsonData

# url = "https://movie.duban.com//j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
# info = ajaxCrawler(url)
# print(info)

for i in (1,11):
    url = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="
    info =ajaxCrawler(url)
    print(len(info))