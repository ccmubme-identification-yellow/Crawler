
import urllib.request
import unicodedata
import string
import re

from urllib.parse import quote

def SearchFromBaidu(_searchName):   
    searchUrl=str(r'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=')+str(_searchName)
    searchUrl=quote(searchUrl, safe=string.printable)
    page = urllib.request.urlopen(searchUrl)#打开网页
    return page.read()

def FindJpgFromPage(_searchPage):
    reg = r'data-imgurl="(.+?\.jpg)" src'#正则表达式
    reg_img = re.compile(reg)
    imglist = reg_img.findall(str(_searchPage))
    return imglist


def main():
    
    imglist=FindJpgFromPage(SearchFromBaidu(u'男人'))
    for img in imglist:
        print(img)
    return 0







if __name__=="__main__":
    main()