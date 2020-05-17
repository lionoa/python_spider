import requests
from bs4 import BeautifulSoup
import os

#请求头
headers = {'User-Agent':" Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

all_url = 'http://pic.netbian.com'

start_html = requests.get(all_url, headers)

#有些网站需要encoding='utf-8'才能使获取的内容中文不乱码
start_html.encoding='gb18030'

#通过BeautifulSoup来分析获得的内容
Soup = BeautifulSoup(start_html.text, 'lxml')

#使用BeautifulSoup的find()和find_all()方法来获取需要的内容，find表示只寻找一次div标签为'slist'的内容(根据网页分析可以发现所有的图片都在silst中)。
#find_all()表示寻找所有的a标签，先寻找class为slist，然后在此标签中寻找a标签
all_a = Soup.find('div', class_='slist').find_all('a')

#使用循环一次只获取一个a标签中的内容
for a in all_a:
        img_url = a.find('img')['src']      #通过find方法先寻找img中的内容，然后将其中src的内容截取下来
        img = 'http://pic.netbian.com' + img_url        #由于网站问题获取的网址并不是全部网址，通过上个等级的测试可以知道地址可以拼接而成
        r = requests.get(img)       #获取到网址之后就和等级1一样用requests的get方法得到图片的信息
        name = img[-9:-4]+'.jpg'    #这里为图片取名，取倒数第9个到倒数第5个字符为图片名称
        with open(name,'wb') as f:      #以二进制保存图片              
                 f.write(r.content)
