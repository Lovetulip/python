"""
              多队列爬虫
            time:20180506

"""
import threading
import queue as Queue
import os
import re
import download_m3u8 as down
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
browserPath = '/home/tulip/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homePage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = '/home/tulip/photo/'
parser = 'html5lib'

class myThread(threading.Thread):
    
    download_path = down.download_path()
    
    def __init__(self,name,url):
        
        
        threading.Thread.__init__(self)
        
        self.url    = url
        self.name   = name
    def run(self):
        print("start procsee",self.name) 
        while True:
            try:
                
                #data = self.girlsInfo_thread.get()
                down.down_ts(myThread.download_path,self.url.get())
                if self.url.empty():
                    break
            except:
                print("下载出现问题了")
        print("exit ", self.name)


def main():
    url = "https://cdn.zypbo.com/20180803/HIpshdcL/index.m3u8"
    link = []
    link = down.download(url)
    
    Threadlist = ["Thread-1","Thread-2","Thread-3","Thread-4","Thread-5"]
    workQueue  = Queue.Queue()
    threads    = []
    
    for tname in Threadlist:

        thread = myThread(tname,workQueue)
        thread.start()
        threads.append(thread)
    
    for url in link: 
        workQueue.put(url)


    for t in threads:
        t.join()
    
    print("all is finished")






if __name__ == "__main__":
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    main()
