"""
              多队列爬虫
            time:20180506

"""
import threading
import queue as Queue
from core import download as down

class myThread(threading.Thread):
    
    download_path = down.download_path()
    
    def __init__(self,Thread_name,url):
        
        
        threading.Thread.__init__(self)
        
        self.url    = url
        self.Thread_name   = Thread_name
    def run(self):
        print("start procsee",self.Thread_name) 
        while True:
            try:
                
                #data = self.girlsInfo_thread.get()
                #线程中想要得到队列中的内容必须用get方法
                down.down_ts(myThread.download_path,self.url.get())
                
                #如果队列为空就位跳出duil
                if self.url.empty():
                    break
            except:
                print("下载出现问题了,重试一次")
                down.down_ts(myThread.download_path,self.url.get())
        print("exit ", self.Thread_name)


def muit_thread(url):
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
    
    print("all videl  have been  downloaded")






if __name__ == "__main__":
    url = "https://cdn.zypbo.com/20180803/HIpshdcL/index.m3u8"
    muit_thread(url)
