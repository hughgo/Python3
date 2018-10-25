import requests
from bs4 import BeautifulSoup
from lxml import etree


url = "https://movie.douban.com/top250"
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
def Getbyxml(url):
    data = requests.get(url,headers = headers).text
    name = []
    star_con = []
    score =[]
    info = []
    comment_list = []
    response = etree.HTML(data)
    result = response.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li')
    for item in result:
         name_item = item.xpath("./div/div[2]/div[1]/a/span[1]/text()")[0].strip()
         info_name = item.xpath("./div/div[2]/div[2]/p[1]/text()")[0].strip()
         score_item = item.xpath("./div/div[2]/div[2]/div/span[2]/text()")[0].strip()
         star_item = item.xpath("./div/div[2]/div[2]/div/span[4]/text()")[0].strip()
         try:
             comment = item.xpath("./div/div[2]/div[2]/p[2]/span/text()")[0].strip()
             comment_list.append(comment)
         except:
             comment_list.append('无')

         score.append(score_item)
         name.append(name_item)
         star_con.append(star_item)
         info.append(info_name)


    return name,info,score,star_con,comment_list



t=Getbyxml(url)
print(t)









# soup = BeautifulSoup(data , 'html.parser')
# ol = soup.find('ol',class_= 'grid_view') #有序列表：<ol class='grid_view'>

#print(ol)

# for  i  in ol.find_all('li'):
#     detail = i.find('div',attrs={'class':'hd'})
#     name_item = detail.find(
#         'span',attrs={'class':'title'}).get_text()
#     print(name_item)
#     detail2 = i.find('div', attrs={'class': 'bd'})
#     name_item2 = detail2.find(
#          'p', attrs={'class': ''}).get_text()
#     print(name_item2)
#     detail3 = i.find('div', attrs={'class': 'bd'})
#     name_item3 = detail3.find(
#         'span', attrs={'class': 'rating_num'}).get_text()
#     print(name_item3)
#     detail4 = i.find('div', attrs={'class': 'bd'})
#     name_item4 = detail4.find(
#         'span', attrs={'class': 'inq'}).get_text()
#     print(name_item4)
#



