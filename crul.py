"""
    这就是最重要的练习     

    作者：tulip ji


"""
import json 
import csv
import requests
from bs4 import BeautifulSoup


def get_all_city():
    """
        得到所有的城市指数 

    """


    rul = "http://www.pm25.in/"
    city_lsit = []
    r = requests.get(rul,timeout=30)
    soup = BeautifulSoup(r.text,"lxml")
    
    city_div = soup.find_all("div",{"class":"bottom"})[1]
    city_link_list = city_div.find_all("a")
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link["href"][1:]
        city_lsit.append((city_name,city_pinyin))  

    return city_lsit 
def get_httm_text(city_pinyin):

    curl = "http://www.pm25.in/" + city_pinyin
    r = requests.get(curl,timeout=30)
    print(r.status_code)
    soup = BeautifulSoup(r.text,"lxml")
    div_list = soup.find_all("div",{"class":"span1"})
    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find("div",{"class":"caption"}).text.strip()
        value   = div_content.find("div",{"class":"value"}).text.strip()
        #city_aqi.append((caption,value))
        city_aqi.append(value)
    return city_aqi
    
    
    #return r.text



def jason_process(filename):

    f = open(filename,mode="r",encoding="utf-8")
    city_lsit = json.load(f)
    return city_lsit


def main():
    
#    city_name = input("请输入要查询的城市拼音名称",)
#    curl = "http://pm25.in/" + city_name
#
#
#    aqi_dic = "title: '【北京空气质量】  AQI: "
#
#    curl_text = get_httm_text(curl)
#
#    index = curl_text.find(aqi_dic)
#    begin_index = index + len(aqi_dic)
#    end_index = begin_index + 2
#
#    aqi_value = curl_text[begin_index:end_index]
#    print("空气质量为{}".format(aqi_value))


    header = ["city","aqi","pm2.5","pm10","co","no2","o3","03/8h",] 
    city_lsit = get_all_city()
#    for city in city_lsit:
#        city_name = city[0]
#        city_pinyin = city[1]
#        city_aqi= get_httm_text(city_pinyin)
    with open ("aqi.csv","w",encoding="utf-8",newline="") as f :
        writer = csv.writer(f)
        writer.writerow(header)
        for i , city in enumerate (city_lsit):
            if (i+1) % 10 == 0:
                print("已经处理{},共{}".format(i+1,len(city_lsit)))
            city_name = city[0]
            city_pinyin = city [1]
            city_aqi = get_httm_text(city_pinyin)
            row = [city_name] + city_aqi
            writer.writerow(row)
    
    
if __name__ == "__main__":
    main()



