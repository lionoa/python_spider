import requests
from bs4 import BeautifulSoup
import os
#导入要用到的库

headers = {'User-Agent':" Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
#请求头

same_url = 'http://pic.netbian.com/index_'   #该网站每个网页的网址中相同的部分

for i in range(2,50):   #用循环得到各个页数的网址，每个页数获取一次信息并下载图片，这里获取49页
    url = same_url+str(i)+'.html'  
    start_html = requests.get(url, headers)     #与网页连接
    start_html.encoding='gb18030'       #获取的网页内容不会中文乱码
    Soup = BeautifulSoup(start_html.text, 'lxml')       #获取网页内容
    all_a = Soup.find('div', class_='slist').find_all('a')      #这里先搜索   class='slist'   的 div  标签，接着获取<a><\a>标签中的内容
    for a in all_a:       
            img_url = a.find('img')['src']         #得到图片下载地址，该网站显示在标签中的网址内容只有后半部分原因，所以需要拼接
            img = 'http://pic.netbian.com' + img_url        #拼接网址
            r = requests.get(img)       #通过图片网址得到图片的信息
            name = img[-9:-4]+'.jpg'        #这里取名用最后第九个字符到第四个字符   
            with open(name,'wb') as f:      #将图片的信息以二进制存入文件         
                    f.write(r.content)
