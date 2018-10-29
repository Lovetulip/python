

from tkinter import *
from tkinter import ttk

class App:

    def __init__(self,root):

        root.title("feet to master")
        mainframe = ttk.Frame(root,padding="3 3 12 12")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)

        self.oam_ip   = StringVar()
        self.oam_vlan = StringVar()
        self.s1_ip    = StringVar()
        self.s1_vlan  = StringVar()
        # 这部分是第一个输入框
        ttk.Label(mainframe,text="oam_ip").grid(column=1,row=1,sticky=(W,E))
        oam_ip_entry = ttk.Entry(mainframe,width=10,textvariable=self.oam_ip)
        oam_ip_entry.grid(column=2,columnspan=2,row=1,sticky=(W,E))
        # this is second input
        ttk.Label(mainframe,text="oam_vlan").grid(column=1,row=2,sticky=(W,E))
        oam_vlan_entry = ttk.Entry(mainframe,width=10,textvariable=self.oam_vlan)
        oam_vlan_entry.grid(column=2,columnspan=2,row=2,sticky=(W,E))
        # the third inout

        ttk.Label(mainframe,text="s1_ip").grid(column=1,row=3,sticky=(W,E))
        s1_ip_entry = ttk.Entry(mainframe,width=10,textvariable=self.s1_ip)
        s1_ip_entry.grid(column=2,columnspan=2,row=3,sticky=(W,E))

        ttk.Label(mainframe,text="s1_vlan").grid(column=1,row=4,sticky=(W,E))
        s1_vlan_entry = ttk.Entry(mainframe,width=10,textvariable=self.s1_vlan)
        s1_vlan_entry.grid(column=2,columnspan=2,row=4,sticky=(W,E))


        #th button control
        ttk.Button(mainframe,text="获取",command=self.callbutton).grid(column=2,row=5,sticky=W)
        ttk.Button(mainframe,text="清空",command=self.clear).grid(column=3,row=5,sticky=W)
        # 每个组件的距离是5px
        
        for child in  mainframe.winfo_children():
            child.grid_configure(padx=5,pady=5)
    def get_ip(self):
        h = self.oam_ip.get()
        return h
    def callbutton(self):
        print(self.oam_ip.get(),self.oam_vlan.get(),self.s1_ip.get(),self.s1_vlan.get())
    def clear(self):
        http = "http"
        self.oam_ip.set(http)
        self.oam_vlan.set("")
        self.s1_ip.set("")
        self.s1_vlan.set("")



#uname_entry.focus()
root = Tk()
app  = App(root)
root.mainloop()

print ("test")
print(app.get_ip())
if "__name__" == "__main__":
    main()
