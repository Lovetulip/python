
import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
browserPath = '/home/tulip/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
homePage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = '/home/tulip/photo/'
parser = 'html5lib'


def main():

    driver = webdriver.PhantomJS(executable_path=browserPath) 
    driver.get(homePage)  
    bsObj = BeautifulSoup(driver.page_source, parser)
    print ("[*] ok get home page ")

    ## 获得主页上所有妹子的姓名、所在城市、身高、体重等信息
    girlslist = driver.find_element_by_id("J_GirlsList").text.split("\n")

    #获取所有妹子的封面图片

    imagesUrl = re.findall('\/\/gtd\.alicdn\.com\/sns_logo.*\.jpg',driver.page_source)

    #解析出妹子的个人主页地址等信息
    girlsUrl = bsObj.find_all("a",{"href": re.compile("\/\/.*\.htm\?(userId=)\d*")}) 

    girlsNL = girlslist[::3]
    # 所有妹子的身高体重
    girlsHW = girlslist[1::3]
    # 所有妹子的个人主页地址
    girlsHURL = [('http:' + i['href']) for i in girlsUrl]
    # 所有妹子的封面图片地址
    girlsPhotoURL = [('https:' + i) for i in imagesUrl]

    girlsInfo = zip(girlsNL, girlsHW, girlsHURL, girlsPhotoURL)

    # 姓名地址      girlNL，  身高体重 girlHW
    # 个人主页地址  girlHRUL, 封面图片 
    
    for girlNL , girlHW , girlHRUL , girlCover in girlsInfo:

        print("[*]:",girlNL,girlHW)
        # 为妹子建立文件夹
        mkdir(outputDir + girlNL)
        print("    [*]saving... ")
        # 获取妹子封面图片
        data = urlopen(girlCover).read()
        with open(outputDir + girlNL + '/cover.jpg', 'wb') as f:
            f.write(data)
        print("    [+]Loading Cover...  ")
        # 获取妹子个人主页中的图片
        getImgs(girlHRUL, outputDir + girlNL)
    driver.close()

def getImgs(url,path):
        
        print("test get ",url,path)
        driver = webdriver.PhantomJS(executable_path=browserPath)
        
        driver.get(url)
        print("[*]open ....")
        bsObj = BeautifulSoup(driver.page_source,parser)

        imgs = bsObj.find_all("img",{"src":re.compile(".*\.jpg")})

        for i , img in enumerate(imgs[1:]):

            try :
                html = urlopen('https:' + img['src'])
                data = html.read()
                fileName = "{}/{}.jpg".format(path, i + 1)
                print("    [+]Loading...", fileName)
                with open(fileName, 'wb') as f:
                    f.write(data)
            except Exception:

                print("    [!]Address Error! ")
        driver.close()




def mkdir(path):

    isexists = os.path.exists(path)

    if not isexists :

        print(  "[*]新建了文件夹)",path)
        os.makedirs(path)        
    else :

        print ("文件夹已经存在")


    







if __name__ == "__main__":
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    main()
