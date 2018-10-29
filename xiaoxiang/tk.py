

from tkinter import *
from tkinter import ttk

def callbutton():
    print(oam_ip.get(),oam_vlan.get(),s1_ip.get(),s1_vlan.get())

def clear():
    oam_ip.set("")
    oam_vlan.set("")
    s1_ip.set("")
    s1_vlan.set("")

def windos():
    root = Tk()
    root.title("feet to master")

    mainframe = ttk.Frame(root,padding="3 3 12 12")
    mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
    mainframe.columnconfigure(0,weight=1)
    mainframe.rowconfigure(0,weight=1)

    oam_ip   = StringVar()
    oam_vlan = StringVar()
    s1_ip    = StringVar()
    s1_vlan  = StringVar()
    # 这部分是第一个输入框
    ttk.Label(mainframe,text="oam_ip").grid(column=1,row=1,sticky=(W,E))
    oam_ip_entry = ttk.Entry(mainframe,width=10,textvariable=oam_ip)
    oam_ip_entry.grid(column=2,columnspan=2,row=1,sticky=(W,E))
    # this is second input
    ttk.Label(mainframe,text="oam_vlan").grid(column=1,row=2,sticky=(W,E))
    oam_vlan_entry = ttk.Entry(mainframe,width=10,textvariable=oam_vlan)
    oam_vlan_entry.grid(column=2,columnspan=2,row=2,sticky=(W,E))
    # the third inout

    ttk.Label(mainframe,text="s1_ip").grid(column=1,row=3,sticky=(W,E))
    s1_ip_entry = ttk.Entry(mainframe,width=10,textvariable=s1_ip)
    s1_ip_entry.grid(column=2,columnspan=2,row=3,sticky=(W,E))

    ttk.Label(mainframe,text="s1_vlan").grid(column=1,row=4,sticky=(W,E))
    s1_vlan_entry = ttk.Entry(mainframe,width=10,textvariable=s1_vlan)
    s1_vlan_entry.grid(column=2,columnspan=2,row=4,sticky=(W,E))


    #th button control
    ttk.Button(mainframe,text="获取",command=callbutton).grid(column=2,row=5,sticky=W)
    ttk.Button(mainframe,text="清空",command=clear).grid(column=3,row=5,sticky=W)
    # 每个组件的距离是5px
    for child in  mainframe.winfo_children():
        child.grid_configure(padx=5,pady=5)

    #uname_entry.focus()
    root.mainloop()
def main():
    windos()
if "__name__" == "__main__":
    main()
