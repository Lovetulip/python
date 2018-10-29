"""
    这就是最重要的练习     

    作者：tulip ji


"""
import json 
import csv
def jason_process(filename):

    f = open(filename,mode="r",encoding="utf-8")
    city_lsit = json.load(f)
    return city_lsit


def main():
    
    filename = input("请输入Jason文件名",) 
    
    aqi_list = jason_process(filename)
    aqi_list.sort(key=lambda city: city["aqi"])
    
    lines = []
    lines.append(list(aqi_list[0].keys()))

    for city in aqi_list:
        lines.append(list(city.values()))

    f = open("aqi.csv","w",encoding="utf-8",newline="")
#    write = csv.writer(f)
    for line in lines:
        f.csv.writerow(line)
    f.close

    print(aqi_list)



    
    
if __name__ == "__main__":
    main()



