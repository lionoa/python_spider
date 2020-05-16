#encoding='utf-8'
    
#导入相关的库
import requests
from bs4 import BeautifulSoup
import os
    
url = "http://pic.netbian.com/uploads/allimg/180222/231102-15193122629634.jpg"
    
#定义请求头，自己电脑的请求头可以在开发者工具中查看，点击最上方一栏的Network,然后右下角的部分往下划，最底下就是你电脑的请求头。
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    
#使用requests中的get方法来获取url的内容
response = requests.get(url, headers)

#保存图片使用二进制方法content
r = response.content

#保存图片
with open("娑娜.jpg",'wb') as f:
    f.write(r)
