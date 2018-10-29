"""
    editorer : tulip ji
    data :  2017.12.17


"""

import turtle 
#import turtle.forward as mpl
#mpl.use("TkAgg") # Use TKAgg to show figures
def tree(branch_length):

    if branch_length > 5:
        # right branch
        turtle.forward(branch_length)     
        turtle.right(20)
        tree(branch_length-15)        


        # left branch 
        print("向左40度")
        turtle.left(40)

        tree(branch_length - 15)

    # return point 
        print("向后右20度")
        turtle.right(20)

        print("向后距离",branch_length)
        turtle.backward(branch_length)


def drw_start_recursive(size):
    count = 1

    while count <= 5 :
        turtle.forward(size)
        turtle.right(144)
        count = count + 1
    size+=20
    if size <= 200:
        drw_start_recursive(size)


def drw_start(size):
    count = 1

    while count <= 5 :
        turtle.forward(size)
        turtle.right(144)
        count = count + 1



def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(300)
    turtle.pendown()
    turtle.pencolor("red")
   
    
    tree(100)

#    turtle.pencolor("red")
###    while size_start <= 200:
#        drw_start(size_start)
#        size_start+=20
    turtle.exitonclick()




if __name__ == "__main__":
    main()
else:
    print("error")
