import pickle as p
import tkinter.messagebox as mb
import os 
from  tkinter import *
val=[]
def call():
    global val
    os.system("python3 Desktop/nettest.py")
    with open("nettesttxt.dat","rb") as fo3 :
        l=len(fo3.read())
        fo3.seek(0)
        while l!=fo3.tell():  
                fc=p.load(fo3)
                val.append(fc)
        mb.showinfo("your internet speed",f"download :{val[-3]}mbps\nupload :{val[-2]}mbps\nping :{val[-1]}ms") 
def history1():
    mb.showinfo("your internetspeed test history ",val) 
    root2.destroy()           
def process():
    mb.showinfo(" process call","your internet speedtest is processing  it may take 25 sec ")
    call()
    root.destroy()

root=Tk()
root.geometry("200x100")
root.title("speedtest")
Button(root,text="go",activebackground="black",command=process).pack()
root.mainloop()
root2=Tk()
root2.title("history")
v1=Button(root2,text="wanna see your history ?",command=history1)
v2=Button(root2,text="quit?",command=root2.destroy)
v1.pack(side=RIGHT)
v2.pack(side=LEFT)
root2.mainloop()

