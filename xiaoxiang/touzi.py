"""
    2018第一天工作
    想要更好的努力
    加油tulip


"""
# -*- coding: utf-8 -*- 
import random
import matplotlib.pyplot as plt
plt.rcParams["axes.unicode_minus"] = False
zhfont = plt.font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')
plt.rcParams['font.sans-serif'] = ['zhfont']
def roll():

    result_list = random.randint(1,6)

    return result_list


def main():
    a=6
    total_time = 100
    
    value_result_list = [0] * 11
   
    roll_list = list(range(2,13))
    roll_dict = dict(zip(roll_list,value_result_list))
    result_list1 = []
    result_list2 = []
    zhifang_list = []

    for i in range(total_time):
        roll1 = roll()
        roll2 = roll()

#        result_list1.append(roll1)
#        result_list2.append(roll2)
        zhifang_list.append(roll1 + roll2)
#        for j in range(2,13):

 #           if j == (result_list1 + result_list2):
  #              roll_dict[j] += 1
   # for x , y in roll_dict.items():

    #    print("{}---{}".format(x,y))

#    x = range(1,total_time+1) 
 #   plt.scatter(x,result_list1,alpha=0.5,c="red")
  #  plt.show()
    
    plt.hist(zhifang_list,bins=range(2,14),edgecolor="black")
    plt.title("你猜猜")
    plt.xlabel("不知道")
    plt.ylabel("呵呵")
    plt.show()
    
if __name__ == "__main__":
    main()
else:
    print(error)
