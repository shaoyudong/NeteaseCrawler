# -*- coding: utf-8 -*-
import urllib
import urllib.request
from lxml import etree

urllib2 = urllib.request
url = 'http://news.163.com/special/0001386F/rank_news.html'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
    html = html.decode("gb2312")
    html = etree.HTML(html)
    result = html.xpath("//div[@class='area-half right']/div/div[contains(@class,'tabContents')][1]//a/@href")  #读取到所有新闻标题
    print(result)
    print(len(result))
    # print(etree.tostring(result[0], encoding="gb2312").decode("gb2312"))
except urllib2.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)