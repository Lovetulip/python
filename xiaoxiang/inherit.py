"""

    今天一定要把继承学会

"""

from tkinter import *

from tkinter import ttk

class User:
    def __init__(self,root):
        mainframe = ttk.Frame(root,padding="3 3 12 12")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)

        oam_ip   = StringVar()

        ttk.Label(mainframe,text="oam_ip").grid(column=1,row=1,sticky=(W,E))
        oam_ip_entry = ttk.Entry(mainframe,width=10,textvariable=oam_ip)
        oam_ip_entry.grid(column=2,columnspan=2,row=1,sticky=(W,E))

root = Tk()
user = User(root)

root.mainloop()

if __name__ == "__main__":
    main()
