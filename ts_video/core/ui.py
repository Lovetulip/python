from core import kankanwu
from core import muit_down
import random
from tkinter import *
from tkinter.ttk import *

video_link = kankanwu.get_video_link()
root = Tk()
lb_movie      = Listbox(root)
def Callon(event):
    root1=Tk()
    root1.title("test")
    Label(root1,text='你选择的电影'+"《"+lb_movie.get(lb_movie.curselection())+"》"  "准备下载！").pack()
    Button(root1,text='好的,知道了',command=root1.destroy).pack()


def refresh():

    new_movie = random.randint(40,70)
    lb_movie.insert(1,video_link[new_movie][0])  
    
def down_video():

    print(lb_movie.curselection()[0])
    print(video_link[int(lb_movie.curselection()[0])][1])
    
    click_movie_link = kankanwu.get_source_link(video_link[int(lb_movie.curselection()[0])][1])
    if ".m3u8" in click_movie_link:
        muit_down.muit_thread(click_movie_link)
    else:
        print("link has error")

def run():

    #root = Tk()
    root.title("this is down video")
    #root.config(background = "blue")
    #root.resizable(False,True)

    label_video = Label(root,text="video")
    label_video.grid(row=0,column=0,padx=10,pady=10)

    #lb_movie      = Listbox(root)
    lb_movie.grid(row=2,column=0,padx=5,pady=10)

    lb_movie.bind('<Double-Button-1>',Callon)
    for i in range(0,40):
        lb_movie.insert(END,video_link[i][0])



    lb_info       = Listbox(root)
    lb_info.grid(row=7,column=0,padx=5,pady=10)

    label_tilte = Label(root,text ="this is advice")
    label_tilte.grid(row=6,column=0,padx=10,pady=10)

    frm = Frame(root)
    frm.grid(row=8,column=0)
    button_refresh = Button(frm,text = "refresh ",command=refresh)
    button_refresh.grid(row=9,column=0,padx=5,pady=5)

    button_download= Button(frm,text = "down",command=down_video)
    button_download.grid(row=9,column=1,padx=5,pady=5)

    button_quit    = Button(frm,text = "quit",command=root.destroy)
    button_quit.grid(row=9,column=2,padx=5,pady=5)

    root.mainloop()
