import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from urllib import request
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browserPath = '/home/tulip/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homePage    = 'http://www.goudaitv.com/frim/index1.html'
parser      = 'html.parser'

def Browser(homePage):
    service_args=[]
    #关闭图片加载
    service_args.append('--load-images=no')
    #开启缓存
    service_args.append('--disk-cache=yes')
    #忽略https错误
    service_args.append('--ignore-ssl-errors=true') 

    #phantomjs 的存放路径
    browserPath = '/home/tulip/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs' 
    #配置代理IP和端口
    #service_args.append('--proxy=www-proxy.ericsson.se:8080')
    #配置代理方式为http
    #service_args.append('--proxy-type=http')

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.loadImages"] = False
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    
    #调用打开无头浏览器
    driver = webdriver.PhantomJS(executable_path=browserPath,service_args=service_args,desired_capabilities=dcap)

    #模拟访问网址
    driver.get(homePage)

    return driver.page_source

def get_video_link():
    video_link = []
    for i in range(1,4):
        website_adress ="https://www.kankanwu.com/Comedy/index_1_______" + str(i)  + ".html" 
        #print(website_adress)
        print(i)
        bsObj = BeautifulSoup(Browser(website_adress), parser)
        #findall the link of video forexample"movie/index58076.html"
        title_elemnet= bsObj.find_all("a",class_="play-img")
        for  i in range(0,24):
            #this can get "movie/index58076.html"
            movie_link   = title_elemnet[i]["href"]
            movie_title  = title_elemnet[i].img["alt"]
            #get the number of movie
            #Num_link     = re.findall("\d+",movie_link)[0]
            # we can split joint play address by num ,
            play_link    = "https://www.kankanwu.com" + movie_link + "player-0-0.html"
            video_link.append((movie_title,play_link))
        else:
            pass

    return video_link
#this function can get source link to read video directly
def get_source_link(video_link):
    bsObj         = BeautifulSoup(Browser(video_link), parser)
    title_elemnet = bsObj.find_all("iframe")
    #'https://newplayers.pe62.com/mdparse/m3u8.php?id=https://youku163.zuida-bofang.com/20180730/10418_90c9f507/index.m3u8'
    source_link   = title_elemnet[0]["src"]
    #ts video link 
    print(source_link)
    ts_video_link = source_link.split("=",1)[-1]
   
    return ts_video_link
def save_video_link_totext(abc):

    file_path = os.path.dirname(os.path.abspath(__file__)) + "/link.txt"
    with open(file_path,"w+") as f:
        f.write(abc)



if __name__ == "__main__":

    video_link = get_video_link()
    for index,link  in enumerate(video_link):
        print("run{}",index,link)
