
import time
import threading
import queue as Queue

class myThread(threading.Thread):

    def __init__(self,name,girlHRUL):

        threading.Thread.__init__(self)
        self.girlHRUL = girlHRUL
        self.name      = name
    def run(self):
        print("start procee",self.name)
        
        while True:
            try :

                print_time(self.name,self.girlHRUL)
                if self.girlHRUL.empty():
                    break
            except:
                break
        print("exit",self.name)
def print_time(name,girlHRUL):
    try:
        data = girlHRUL.get()
        print(name)
        return print("main",data)
    except Exception as e:
        print("errorsssssssssss",e)


Threadlist = ["Thread-1","Thread-2"]
workQueue  = Queue.Queue()
threads    = []




for tname in Threadlist:

    thread = myThread(tname,workQueue)
    thread.start()
    threads.append(thread)
for url in range(10):
    workQueue.put(url)
for t in threads:
    t.join()

print("all is finished")
