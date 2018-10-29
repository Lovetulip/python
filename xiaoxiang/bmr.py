"""
    bmr Process


"""
import time 
def timer(bmr):
    print("first")
    def desc():
        start = time.time()
        bmr()
        stop = time.time()
        print("time is %s"%(stop - start))
    return desc 

@timer
def bmr():


    y_or_n = input("是否退出程序y/n")

    while y_or_n !="y" :
        print("请输入以下信息,用空格分割")

        input_str = input("性别 体重 身高 年龄")

        str_list = input_str.split(" ")
        try:

            gender = str_list[0]

            weigh = float(str_list[1])

            high = float(str_list[2])

            age = int(str_list[3])
            
            if gender == "男":

                bmr = (13.7 * weigh) + (5.0 * high) - (6.8 * age) + 66

            elif gender == "女":

                bmr = (9.6 * weigh) + (1.8 * high) - (4.7 * age) +655
            else:
                bmr = -1
            if bmr != -1:

                print("您的性别：{},体重{}公斤,身高{}厘米,年龄{}岁".format(gender,weigh,high,age))
                print("您的基础代谢率{}打卡",format(bmr))

            else:

                print("不支持性别")

        except ValueError:
            print("请输入正确信息")


        y_or_n = input("是否退出程序Y/Q")           
            


def main():

    bmr()



if __name__ == "__main__":
    main()
else:
    print("err")
