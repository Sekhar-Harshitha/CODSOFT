from tkinter import *

root=Tk()
root.title("CALCULATOR")
a=Entry(root,width=50,borderwidth=5,fg="black",bg="white")
a.grid(row=0,column=0,columnspan=4)

def click(num):
    inp=a.get()
    a.delete(0,END)
    a.insert(0,str(inp)+str(num))
    return

def clear():
    a.delete(0,END)
    return

def bksp():
    current=a.get()
    length=len(current)-1
    a.delete(length,END)

def evaluate():
    ans=a.get()
    ans=eval(ans)
    a.delete(0,END)
    a.insert(0,ans)

b_clear=Button(root,text="C",padx=25,pady=10,command=clear,fg="white",bg="black")
b_BK=Button(root,text="X",padx=25,pady=10,command=bksp,fg="white",bg="black")
b_percentage=Button(root,text="%",padx=25,pady=10,command=lambda: click("%"),fg="white",bg="black")
b_divide=Button(root,text="/",padx=25,pady=10,command=lambda: click("/"),fg="white",bg="black")

b_7=Button(root,text="7",padx=25,pady=10,command=lambda: click(7),fg="white",bg="black")
b_8=Button(root,text="8",padx=25,pady=10,command=lambda: click(8),fg="white",bg="black")
b_9=Button(root,text="9",padx=25,pady=10,command=lambda: click(9),fg="white",bg="black")
b_multiply=Button(root,text="*",padx=25,pady=10,command=lambda: click("*"),fg="white",bg="black")

b_4=Button(root,text="4",padx=25,pady=10,command=lambda: click(4),fg="white",bg="black")
b_5=Button(root,text="5",padx=25,pady=10,command=lambda: click(5),fg="white",bg="black")
b_6=Button(root,text="6",padx=25,pady=10,command=lambda: click(6),fg="white",bg="black")
b_sub=Button(root,text="-",padx=25,pady=10,command=lambda: click("-"),fg="white",bg="black")

b_1=Button(root,text="1",padx=25,pady=10,command=lambda: click(1),fg="white",bg="black")
b_2=Button(root,text="2",padx=25,pady=10,command=lambda: click(2),fg="white",bg="black")
b_3=Button(root,text="3",padx=25,pady=10,command=lambda: click(3),fg="white",bg="black")
b_add=Button(root,text="+",padx=25,pady=10,command=lambda: click("+"),fg="white",bg="black")

b_zero=Button(root,text="0",padx=40,pady=10,command=lambda: click(0),fg="white",bg="black")
b_point=Button(root,text=".",padx=25,pady=10,command=lambda: click("."),fg="white",bg="black")
b_equal=Button(root,text="=",padx=25,pady=10,command=evaluate,fg="white",bg="black")

b_clear.grid(row=1,column=0,sticky="nsew")
b_BK.grid(row=1,column=1,sticky="nsew")
b_percentage.grid(row=1,column=2,sticky="nsew")
b_divide.grid(row=1,column=3,sticky="nsew")

b_7.grid(row=2,column=0,sticky="nsew")
b_8.grid(row=2,column=1,sticky="nsew")
b_9.grid(row=2,column=2,sticky="nsew")
b_multiply.grid(row=2,column=3,sticky="nsew")

b_4.grid(row=3,column=0,sticky="nsew")
b_5.grid(row=3,column=1,sticky="nsew")
b_6.grid(row=3,column=2,sticky="nsew")
b_sub.grid(row=3,column=3,sticky="nsew")

b_1.grid(row=4,column=0,sticky="nsew")
b_2.grid(row=4,column=1,sticky="nsew")
b_3.grid(row=4,column=2,sticky="nsew")
b_add.grid(row=4,column=3,sticky="nsew")

b_zero.grid(row=5,column=0,columnspan=2,sticky="nsew")
b_point.grid(row=5,column=2,sticky="nsew")
b_equal.grid(row=5,column=3,sticky="nsew")

root.mainloop()
