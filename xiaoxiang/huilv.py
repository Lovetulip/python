# -*- coding: utf-8 -*-
#huilv

#while current_str_value != "Q" :
    #rmb_value = eval(current_str_value)

def convert_current(inmony,huilv):
    out_mony = inmony * huilv
    return out_mony

"""
pratcise def  


"""

def main():
    usd_vs_rmb=6.77
    current_str_value = input('请输入带单位的货币金额(输入Q退出本程序)：')
    value = current_str_value[-3:]
    input_value = 78.001
    input_value = current_str_value[:-3]

    if value == "CNY":
        
        exchange = 1 / usd_vs_rmb


    elif value == "USD":

        exchange = 1 * usd_vs_rmb

    else :
        exchange = -1 

    if exchange != -1 :
         mony = eval(input_value)
         convert_current2 = lambda x : x * exchange
         out = convert_current2(mony)
         print("得到的金额是:",out)
    else: 
        print("本软件不支持")

if __name__ == "__main__":
    main()

#else: 
 #   print ("error")
