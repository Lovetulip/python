

from tkinter import *

root = Tk()

def reg():
    account = account_input.get()
    passpd  = passpd_input.get()

    t1 = len(account)
    t2 = len(passpd)

    if account =="111" and passpd =="222":
        c["text"] = "success"
    else:
        c["text"] = "failure"
        account_input.delete(0,t1)
        passpd_input.delete(0,t2)


account = Label(root,text= "account")
account.grid(row=0 , column = 0 , sticky = W) 

account_input = Entry(root)
account_input.grid(row=0,column=1,sticky = E)

passpd  = Label(root,text = "password")
passpd.grid(row=1,column=0,sticky=W)

passpd_input = Entry(root)
passpd_input.grid(row=1,column=1,sticky=W)
passpd_input["show"] = "*"

bu = Button(root,text = "login in ",command = reg)
bu.grid(row=3,column=3,sticky=E)

c = Label(root,text="")
c.grid(row = 5,sticky=E)

root.mainloop()
