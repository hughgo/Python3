import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename =r"C:\fle\file2.html")

#urlretrieve在执行过程中当中，会产生一些缓存
#清除缓存
urllib.request.urlcleanup()