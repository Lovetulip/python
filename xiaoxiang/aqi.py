"""
    这就是最重要的练习     

    作者：tulip ji


"""
def cal_lines(iaqi_lo,iaqi_hi,bp_lo,bp_hi,cp):
    """
        空气质量计算公式

        
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi 




def cal_pm(pm_val):
    
    """
        计算pm2.5的公式函数
    
    """
    print("cal函数pm",pm_val)
    if 0 <= pm_val < 36:
        iaqi_pm = cal_lines(0,50,0,35,pm_val)
    if 36 <= pm_val <76:
        iaqi_pm = cal_lines(50,100,75,35,pm_val)
    return iaqi_pm

def cal_co(co_val):

    if 0<= co_val < 3:
        iaqi = cal_lines(0,50,0,3,co_val)
    else:
        pass 
    return iaqi

        

def cal_aqi(param_list):
    
    cal_aqi_pm = param_list[0]
    cal_aqi_co = param_list[1]

    pm_iaqi = cal_pm(cal_aqi_pm)
    co_iaqi = cal_co(cal_aqi_co)
    
    aqi_list = []
    aqi_list.append(pm_iaqi)
    aqi_list.append(co_iaqi)

    aqi = max(aqi_list)
    return aqi


def main():
    
    print("请输入pm2.5浓度和co浓度用空格隔离")
    aqi_list = input("pm2.5 co ")
    aqi_list_str = aqi_list.split(" ")
    pm_value = float(aqi_list_str[0])
    co_value = float(aqi_list_str[1])    

    param_list = []

    param_list.append(pm_value)
    param_list.append(co_value)

    pm = cal_aqi(param_list)
    print(pm)

if __name__ == "__main__":
    main()



