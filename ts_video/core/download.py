"""

    this is just for download m3u8 file and ts video
    data 20180808
    author tulio ji 

"""
import  os
import  re
import  sys
import  time 
import  wget
import  random
import  datetime
import  requests
from    binascii import b2a_hex,a2b_hex


header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'}

def download_path():
    download_path = os.getcwd() + "/download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    #new add time file 
    download_path = os.path.join(download_path,datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    #creat file 
    os.mkdir(download_path)
    return download_path

def download(url):

    #get first layers content
    all_content = requests.get(url).text 

    if "#EXTM3U" not in all_content:
        raise BaseException("非M3U8的链接")
    #针对需要两层们u8文件或者加密类型的m3u8
    #在看看屋案例中没有用的39-43 代码
    if "EXT-X-STREAM-INF" in all_content:
        file_line = all_content.split("\n")
        for line in file_line:
            if ".m3u8" in line:
                url = url.rsplit("/",1)[0] + "/" + line 
                all_content = requests.get(url).text
    #现在开始拼凑真是的视频网址
    file_line = all_content.split("\n")
    #因为m3u8文件是很多行，所以以行来区分内容，但是还会包含/r 字符
    #构造一个列表来存贮ts视频网址
    link   = []
    for index , line  in enumerate(file_line):
        if "EXTINF" in line:
            
            #拼凑下载ts视频的原始网址
            
            pd_url = url.rsplit("/",1)[0] + "/" + file_line[index+1] 
            
            ##这个必须记住，通过拼凑得到的网址后面会带有“/r” 字符，但是print看不出来
            #必须通过单步调试才能得到完整的显示，所以会造成接下来的下载失败
            pd_url_final = pd_url.rsplit("\r",1)[0]
            link.append(pd_url_final)
    return link

def down_ts(download_path,link):
 
    unknow = False
    print("start to download video")
    #备用下载方法result=wget.download(i)
    
    ts_video = requests.get(link,headers=header,stream= True)
    c_full_name = link.rsplit("/",1)[-1]
    
    #为了找出视频的下标
    if c_full_name[-7].isdigit():
        index       = c_full_name[-7:-3]
    else:
        index       = "0" + c_full_name[-6:-3]
    with open(os.path.join(download_path,(index + ".ts")),"wb") as f:
        f.write(ts_video.content)
        f.flush
        
        #认为设定随机睡眠时间
        time.sleep(random.uniform(2,5))
    if unknow:
        raise BaseException("not link can be found")
    else :
        print("success to download %s video"%index)
# 只能用在Windows 系统下
def merge_file(path):

    os.chdir(path)
    cmd = "copy /b * new.ts"
    os.system(cmd)
    #os.system("del /Q *.ts")
    #os.system("del /Q *.mp4")
    #os.rename("new.tmp ","new.mp4")

if __name__ == "__main__" :
    url = "https://cdn.zypbo.com/20180730/q8r6mLJp/index.m3u8"
    download(url)


