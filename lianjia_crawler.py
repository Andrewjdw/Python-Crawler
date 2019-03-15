# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:53:46 2018

@author: Andrew
"""
import urllib.request
import re
import csv

def getcontent(url):
    #模拟成浏览器
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
   
    pricepat = r'<div class="main-price">\n[\s]+?<span class="number">(.*?)</span>'    
    namepat = r'target="_blank" data-xftrack="10138">(.*?)</a>'
    namepat = r'<img alt="(.*?)楼盘图片'
    site1pat = r'<div class="resblock-location">\n[\s]+?<span>(.*?)</span>'
    site2pat = r'<i class="split">/</i>[\n\s]+?<span>(.*?)</span>'
    #site3pat = r'data-xftrack="10254">(.*?)</a>'
    #areapat = r'<div class="resblock-area">[\n\s]+?<span>建面\s(.*?)㎡</span>'
    
    pricelist = re.compile(pricepat, re.S).findall(data)
    namelist = re.compile(namepat,re.S).findall(data)
    site1list = re.compile(site1pat,re.S).findall(data)
    site2list = re.compile(site2pat,re.S).findall(data)
    #site3list = re.compile(site3pat,re.S).findall(data)
    #arealist = re.compile(areapat,re.S).findall(data)
    
    
    return namelist, site1list, site2list, pricelist

def save2csv(namelist,site1list,site2list,pricelist):
    with open(r'D:/lianjia.csv','a+', newline='',encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(namelist)):
            writer.writerow([namelist[i], site1list[i], site2list[i],pricelist[i]])

def main(urls):
    count = 0
    for url in urls:
        namelist, site1list, site2list, pricelist = getcontent(url)
        save2csv(namelist, site1list, site2list,  pricelist)
        count += 1
        print("page: "+str(count)+" is writed")
        
        
     
#分别获取各页的段子，通过for循环可以获取多页
if __name__ == '__main__':
    urls = [] 
    for i in range(1,62):
        url='https://nj.fang.lianjia.com/loupan/pg'+str(i)
        urls.append(url)
    main(urls)