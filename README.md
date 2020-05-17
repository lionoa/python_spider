# python_spider


python爬虫爬取网页图片教程
=


以下内容皆为自己的理解，如有错误，请及时告知作者


使用的库：requests、BeautifulSoup、os


目标网站：http://pic.netbian.com

教程
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
            
    #你的娑娜请签收！！！   (>!< )
    
    
    
等级2：通过for循环下载网页的所有图片
    
    代码如下：
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
                     
                     
              
等级3：获取该网站的多个网页的图片，实现批量下载

    
    import requests
    from bs4 import BeautifulSoup
    import os
    #导入要用到的库
   
    #请求头
    headers = {'User-Agent':" Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}


    same_url = 'http://pic.netbian.com/index_'   #这里我们同样是分析网站得到每页网址都是http://pic.netbian.com/index_  加一个数字
    for i in range(2,50):   #用循环得到各个页数的网址，每个页数获取一次信息并下载图片，获取49页，因为第一页没有发现数字所以为了省事就忽略掉第一页
           url = same_url+str(i)+'.html'  
           start_html = requests.get(url, headers)  #与网页连接
           start_html.encoding='gb18030'  #获取的网页内容不会中文乱码
           Soup = BeautifulSoup(start_html.text, 'lxml')    #获取网页内容
           all_a = Soup.find('div', class_='slist').find_all('a')  #获取<a><\a>标签
           for a in all_a:       
                   img_url = a.find('img')['src']	     #得到图片下载地址，网站原因只有部分，所以需要拼接
                   img = 'http://pic.netbian.com' + img_url  #拼接网址
                   r = requests.get(img)	#通过图片地址得到图片的信息
                   name = img[-9:-4]+'.jpg'     #取名最后第九个字符到第五个字符   
                   with open(name,'wb') as f:     #将图片的信息以二进制存入文件         
                           f.write(r.content)
                           
                           
#### 这里建议亲们不要下载太多页数     (!>.<!) 
    
    

            
  
    
    



