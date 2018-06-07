

"""
    练习抓取斗鱼字幕
    练习socket套接字

"""
import multiprocessing
import socket
import time 
import re 
import pymongo 
import requests
from bs4 import BeautifulSoup

clients = pymongo.MongoClient("localhost")
db      = clients["DouyuTV_danmu"]
col     = db["info"]


#构建socket套接字来连接斗鱼弹幕
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host   = socket.gethostbyname("openbarrage.douyutv.com")
port   = 8601
client.connect((host,port))

danmu_path    = re.compile(b"txt@=(.+?)/cid@")
uid_path      = re.compile(b'uid@=(.+?)/nn@')
nickname_path = re.compile(b'nn@=(.+?)/txt@')
level_path    = re.compile(b'level@=([1-9][0-9]?)/sahf')

def sendmsg(msgstr):
    msg         = msgstr.encode("utf-8")
    data_length = len(msg) + 8
    code        = 689
    msgHead     = int.to_bytes(data_length,4,"little") \
    + int.to_bytes(data_length,4,"little")  +  \
    int.to_bytes(code,4,"little")
    
    print("why",msgHead)
    client.send(msgHead)
    sent = 0 
    while sent < len(msg):
        tn   = client.send(msg)
        sent += tn 
def start(roomid):
    msg = "type@=loginreq/username@=rieuse/password@=douyu/roomid@={}/\0".format(roomid)
    sendmsg(msg)
    msg_more = "type@=joingroup/rid@={}/gid@=-9999/\0".format(roomid)
    sendmsg(msg_more)

    print("**************欢迎来的直播间*******************")
    while True:
        data          = client.recv(1024)
        print("************",data)
        uid_more      = uid_path.findall(data)
        nickname_more = nickname_path.findall(data)
        level_more    = level_path.findall(data)
        danmu_more    = danmu_path.findall(data)
        if not level_more:
            level_more = b'0'
        if not data:
            break
        else:
            for i in range(0,len(danmu_more)):
                try:
                    product = {
                        "uid"     :uid_more[0].decode(encoding="utf-8"),
                        "nickname":nickname_more[0].decode(encoding="utf-8"),
                        "level"   :level_more[0].decode(encoding="utf-8"),
                        "danmu"   :danmu_more[0].decode(encoding="utf-8")
                    }
                    print("[{}]:{}".format(nickname_more[0].decode(encoding="utf-8"),danmu_more[0].decode(encoding="utf-8")))
                    #col.insert(product)
                    print("ok")
                except Exception as e:
                    print("occur error",e)
def keeplive():
    while True:
        msg = "type@=keeplive/tick@=" + str(int(time.time())) + "/\0"
        sendmsg(msg)
        time.sleep(30)
def get_name(roomid):

    r = requests.get("http://www.douyu.com/" + roomid )
    soup = BeautifulSoup(r.text,"lxml")
    return soup.find("a",{"class","zb-name"}).string 




if __name__ == "__main__":
    room_id = "1126960"
    p1 = multiprocessing.Process(target=start,args=(room_id,))
    p2 = multiprocessing.Process(target=keeplive)
    p1.start()
    p2.start()
