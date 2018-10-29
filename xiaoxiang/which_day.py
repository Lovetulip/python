"""
    tulip .ji
    data 12/22


"""
import datetime

def judge():
    
    input_data_str = input("请输入想要判断的日期yyyy/mm/dd" )

    input_data = datetime.datetime.strptime(input_data_str,"%Y/%m/%d")

    year = input_data.year

    month = input_data.month

    day = input_data.day

    day_in_year = (31,28,31,30,31,30,31,31,30,31,30,31)
    
    days = sum(day_in_year[:month-1]) + day 
    
    if ( year % 4 == 0) and (year % 100 != 0) or  (year % 400 == 0 ):
        
        if month > 2:

            days += 1

    print("输入日期是一年的第{}天",format(days))









def main():

    judge()

if __name__ == "__main__":
    main()
else:
    print(error)
