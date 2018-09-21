from core import kankanwu
from core import muit_down
from tkinter import *

root = Tk()
root.title("movie list")
root.geometry("300x300")
lb = Listbox(root)

video_link = kankanwu.get_video_link()

#定义右键点击电影名称的操作
def Callon(event):
    root1=Tk()
    root1.title("test")
    Label(root1,text='你选择的电影'+"《"+lb.get(lb.curselection())+"》"  "准备下载！").pack()
    Button(root1,text='好的,知道了',command=root1.destroy).pack()
    
    
    print(lb.curselection()[0])
    print(video_link[int(lb.curselection()[0])][1])
   


    click_movie_link = kankanwu.get_source_link(video_link[int(lb.curselection()[0])][1])
    if ".m3u8" in click_movie_link:
        muit_down.muit_thread(click_movie_link)
    else:
        print("link has error")

def run ():
    #将得到的电影名称存放到video_link方便展示
    
    lb.bind('<Double-Button-1>',Callon)

    #构造显示列表和行动
    for i in range(0,40):
        
        lb.insert(END,video_link[i][0])

    lb.pack()
    root.mainloop()

    #必须设置的，才能最终显示对话框
