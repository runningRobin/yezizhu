# -*- coding:utf-8 -*-
import urllib
import re
import random
import threading

mmurls = []
threads = []

def getMMUrl(url, page=None):
    if not page:
        htmlurl = url
    else:
        htmlurl = url + page
    html = urllib.urlopen(htmlurl).read().decode('gb2312', 'ignore').encode('utf-8')
    reg = r'<a class="picture" href="(.*?)" title='
    urlreg = re.compile(reg)
    urls = re.findall(urlreg, html)
    for murl in urls:
        mmurls.append(murl)
    netpage = re.findall(re.compile(r'<li><a href=\'(.*?)\' target=\'_self\'>下一页</a></li>'), html)
    if netpage:
        getMMUrl(url, netpage[0])
    else:
        getMMImgs()

def getMMImgs():
    for url in mmurls:
        html = urllib.urlopen(url).read().decode('gb2312', 'ignore').encode('utf-8')
        allpage = re.findall(re.compile(r'<li><a>共(.*?)页: </a>'), html)
        allnums = int(allpage[0]) + 1
        getImages(url)
        for i in range(2, allnums):
            getImages(url[:-6] + '_' + str(i) + '.shtml#article')

def getImages(url):
    html = urllib.urlopen(url).read().decode('gb2312', 'ignore').encode('utf-8')
    reg = r'<img border="0" src="(.*?)" alt='
    imgreg = re.compile(reg)
    imgurl = re.findall(imgreg, html)
    path = 'images'
    filename = str(random.randint(1000000000, 9999999999)) + '.jpg'
    if len(imgurl) == 0:
        reg = r'<img border="0" alt="(.*?)" src="(.*?)" />'
        imgreg = re.compile(reg)
        imgurl = re.findall(imgreg, html)
        print len(imgurl[0])
        # if len(imgurl[0]) == 2:
            # print url + ',请耐心等待。。。'
            # urllib.urlretrieve(imgurl[0][1], path + '/' + filename)
        # else:
        #     pass
    else:
        pass
        # print url + ',请耐心等待。。。'
        # urllib.urlretrieve(imgurl[0], path + '/' + filename)




if __name__ == '__main__':
    getMMUrl('http://xx.yzz.cn/xiuba/')
