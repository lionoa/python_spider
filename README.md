# python_spider


python爬虫爬取网页图片教程
=


以下内容皆为自己的理解，如有错误，请及时告知作者


使用的库：requests、BeautifulSoup、os


目标网站：http://pic.netbian.com


首先
-

    分析网站！！！
    
    要爬取一个网站的内容就得从它的网页结构开始，分析网站之后的代码编程就会轻松许多。
    
    进入网站打开开发者工具，按F12或者右键选中检查。
    
    在打开的开发者工具左上角有一个箭头加方框的按钮，点击之后在网页内容部分选中一张图片，选中之后代码会自动跳转到该图片所在位置。
    
    分析这一部分代码可以了解到网站图片所在的代码都在<div class='slist'>...</div>中        
    
    然后再分析<li></li>中的部分
    
    在标签<span></span>中，将鼠标移到src后面的的连接上，鼠标上方是预览图，下方则是图片的地址。
    
    tip:    网站各不相同，如果没有显示地址，不要来找我！！！（—_—）
    
等级1：下载单个网页图片

    通过上述部分可以获得图片的地址，下面随即选一张图片的地址

    #encoding='utf-8'
    
    #导入相关的库
    import requests
    from bs4 import BeautifulSoup
    import os
    
    url = "http://pic.netbian.com/uploads/allimg/180222/231102-15193122629634.jpg
    
    #定义请求头，自己电脑的请求头可以在开发者工具中查看，点击最上方一栏的Network,然后右下角的部分往下划，最底下就是你电脑的请求头。
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    
    #使用requests中的get方法来获取url的内容
    response = requests.get(url, headers)
    
    #保存图片使用二进制方法content
    r = response.content

    #保存图片
    with open("娑娜.jpg",'wb') as f:
            f.write(r)
            
  
    
    



