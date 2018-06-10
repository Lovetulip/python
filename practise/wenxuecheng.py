import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from urllib import request
import eml
browserPath = '/home/tulip/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homePage    = "http://blog.wenxuecity.com/myindex/1666/"
outputDir   = '/home/tulip/wenxuecheng/'
parser      = 'html.parser'
#in order to improve effect
driver = webdriver.PhantomJS(executable_path=browserPath)

#这个函数为了得到首页的每篇博客的链接
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
    service_args.append('--proxy=www-proxy.ericsson.se:8080')
    #配置代理方式为http
    service_args.append('--proxy-type=http')


    #调用打开无头浏览器
    driver = webdriver.PhantomJS(executable_path=browserPath,service_args=service_args)
    #模拟访问网址
    driver.get(homePage)

    return driver.page_source

def get_blog_link():

    #driver = webdriver.PhantomJS(executable_path=browserPath)
    #driver.get(homePage)
    bsObj = BeautifulSoup(Browser(homePage), parser)
    #得到博客首页所有文章的链接
    title_elemnet= bsObj.find_all("div",class_="menuCell_main")
    #将链接提取出来，保存到列表中
    title_list = []
    for i in range(10):
        print("得到的第%s文章链接"%(i+1))
        title_link = str(title_elemnet[i].a["href"])
        title_link_complete = "http://blog.wenxuecity.com" + title_link
        title_list.append(title_link_complete)
        print(title_link_complete)
    return title_list

#这个函数为了获得每一篇博文的正文
def get_blog_content(link_list):

        for index,link in enumerate(link_list):
            #driver = webdriver.PhantomJS(executable_path=browserPath)
            #driver.get(link)
            bsObj    = BeautifulSoup(Browser(link), "html.parser")
            #通过正则表达式提取包含标题和正文的标签
            title    = bsObj.find_all("div",class_="titleinfo")
            content  = bsObj.find("div",class_="articalContent")
            #提取博客文章的题目
            blog_tit = title[0].text.strip().split("\n")[0]
            #提取博客的正文内容
            blog_txt = content.text.strip()
            if os.path.exists(outputDir + str(blog_tit) + ".txt"):
                print("文章《%s》不是最新的，已经存在了"%blog_tit)
            else:
                with open(outputDir + str(blog_tit) + ".txt","w+") as f :
                    print("正则保存第%s篇博文"%(index+1),blog_tit)
                    f.write(blog_txt)
            eml.sendemail("401022627@qq.com","so what?",outputDir + str(blog_tit) + '.txt')

#这个视为多线程写的方便使用，区别在于这个是每次传入一个网址链接
def get_blog_content_muit(link_single):


    #driver = webdriver.PhantomJS(executable_path=browserPath)
    #driver.get(link)
    bsObj    = BeautifulSoup(Browser(link_single), "html.parser")
    #通过正则表达式提取包含标题和正文的标签
    title    = bsObj.find_all("div",class_="articalTitle")
    content  = bsObj.find("div",class_="articalContent")
    #提取博客文章的题目
    blog_tit = title[0].text.strip().split("\n")[0]
    #提取博客的正文内容
    blog_txt = content.text.strip()
    with open(outputDir + str(blog_tit) + ".txt","w+") as f :
        print("正则保存第%s篇博文",blog_tit)
        f.write(blog_txt)

def makdir(path):

    isexists = os.path.exists(path)

    if not isexists:

        print("新创建了文件夹%s"%path)
        os.mkdir(path)
    else:

        print("文件夹已经存在")


if __name__ == "__main__":
    link_list = get_blog_link()
    get_blog_content(link_list)
    driver.close()
