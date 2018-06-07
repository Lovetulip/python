"""
    editor ; tulip ji 

    data : 2017/12/19


"""

import math
import datetime

def save_money_in(money_per_week,money_increase,total_week):
    



    money_list = []
    saving_mony_list=[]


    for i in range(total_week):
        #
        money_list.append(money_per_week)

        save_money = math.fsum(money_list)

        saving_mony_list.append(save_money)
        
        money_per_week += money_increase

    return saving_mony_list


def main():

    money_per_week = float(input("请输入每周存入的金额: "))

    money_increase = float(input("请输入每周的递增金额: "))

    total_week = int(input("请输入总周数: "))

    saving_mony_list = save_money_in(money_per_week , money_increase , total_week)
   
    input_date_str = input("请输入日期:(yyyy/mm/dd):")

    input_date = datetime.datetime.strptime(input_date_str,"%Y/%m/%d")

    week_num = input_date.isocalendar()[1]


   
    print("第{}周存钱{}元".format(week_num,saving_mony_list[week_num-1]))


    

if __name__ == "__main__":

    main()
else:
    print(error)
