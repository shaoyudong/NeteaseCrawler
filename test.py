# -*- coding: utf-8 -*-
import urllib
import urllib.request
from lxml import etree

urllib2 = urllib.request
url = 'http://news.163.com/special/0001386F/rank_whole.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    h = response.read()
    html = h.decode('gbk')
    html = etree.HTML(html)
    result = html.xpath("//div[@class='area-half right']/div/div[contains(@class,'tabContents')][1]//a/@href")  #读取到所有新闻链接
    print(result)

    # 爬取新闻正文

    num = 0
    while (result) :
        newsURL = result.pop(0)
        print(newsURL)
        request = urllib2.Request(newsURL, headers= headers)
        response = urllib2.urlopen(request)
        h = response.read()
        html = h.decode("gbk")
        html = etree.HTML(html)
        news = html.xpath("//div[@class='post_text']/p/text()")
        if (len(news)) :
            num = num + 1
            fileName = newsURL[newsURL.index("com")+4:-5] + ".txt"
            fileName = fileName.replace("/", "-")
            fileName = "news/" + fileName
            file = open(fileName, "w", encoding="utf-8")
            newsTitle = html.xpath("//h1/text()")
            content = newsTitle[0] + "\n"
            for t in news :
                content = content + t
            file.write(content)
            file.close()
            print(news)
        print(num)
    # commentURL = html.xpath("//div[@class='post_comment_tiecount']/a")
    # print(etree.tostring(commentURL[0], encoding="gbk").decode("gbk"))
    # print(etree.tostring(result[0], encoding="gb2312").decode("gb2312"))
except urllib2.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)