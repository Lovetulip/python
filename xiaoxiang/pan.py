




import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib as mat
zhfont = mat.font_manager.FontProperties(fname="/usr/share/fonts/MyFonts/SIMYOU.TTF")
def main():

    aqi_data = pd.read_csv("aqi.csv")
    print("基本信息")
    print("information",aqi_data.info())


    print("top10",aqi_data["aqi"].max())

    clean_aqi_data = aqi_data[aqi_data["aqi"]>0]
    top10_city = clean_aqi_data.sort_values(by=["aqi"],ascending=False).head(10)

    bottom10_city = aqi_data.sort_values(by=["aqi"],ascending = False).head(10)

    print(top10_city)

    top10_city.to_csv("123.py",index=False)

    top50_city = clean_aqi_data.sort_values(by=["aqi"],ascending=False).head(50)
    top50_city.plot(kind="bar",x="city",y="aqi",figsize=(20,10))
    
    plt.title("我的天",FontProperties=zhfont)
    plt.savefig("top_aqi")
    plt.show()

if __name__ == "__main__":
    main()

















