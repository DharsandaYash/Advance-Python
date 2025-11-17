from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 as sq
import csv

root = Tk()
root.title("SC")
data = ""

def init():
    cnn = sq.connect("MY.db")
    cursor = cnn.cursor()
    cursor.execute("create table if not exists My_Record(id integer primary key autoincrement,name text,price integer)")
    cursor.close()
    cnn.close()
init()

nm = StringVar()
pr = IntVar()
def insert_data():
    name = nm.get()
    price = pr.get()
    a = len(name)
    b =  len(txt2.get())
    if(a>0 and b>0):
        cnn = sq.connect("MY.db")
        cursor = cnn.cursor()
        cursor.execute("insert into My_Record(name,price)values(?,?)",(name,price))
        txt1.delete(0,END)
        txt2.delete(0,END)
        txt1.focus()
        cnn.commit()
        messagebox.showinfo("Information","Record inserted........")
        cursor.close()
        cnn.close()
    else:
        messagebox.showinfo("info","enter data")    

gp1 = LabelFrame(root,text="Insert Records",width="400",height="200",font=("Arial Black",10))
gp1.pack(padx=150,pady=10,fill="x",expand=False)

gp2 = LabelFrame(root,text="Search Records",width="400",height="200",font=("Arial Black",10))
gp2.pack(padx=150,pady=10,fill="x",expand=False)


gp3 = LabelFrame(root,text="All",width="200",height="400",font=("Arial Black",10))
gp3.pack(padx=350,pady=10,fill="both",expand=False)



lbl3 = Label(gp2,text="Enter Something",font=("Calibri",13))
lbl3.place(x=30,y=50)
txt3 = Entry(gp2)
txt3.place(x=160,y=50)



lbl1 = Label(gp1,text="Name",font=("Calibri",13))
lbl1.place(x=30,y=50)
txt1 = Entry(gp1,textvariable=nm)
txt1.place(x=80,y=50)


lbl2 = Label(gp1,text="Price",font=("Calibri",13))
lbl2.place(x=30,y=90)
txt2 = Entry(gp1,textvariable=pr)
txt2.place(x=80,y=90)

btn1 = Button(gp1,text="Save Data",command=insert_data,font=("Arial Black",10))
btn1.place(x=80,y=130)

btn2 = Button(gp2,text="Search",font=("Arial Black",10))
btn2.place(x=120,y=90)
btn4 = Button(root,text="Update",font=("Arial Black",10))
btn4.place(x=350,y=900)
btn3 = Button(root,text="Delete",font=("Arial Black",10))
btn3.place(x=450,y=900)
btn5 = Button(root,text="Export",font=("Arial Black",10))
btn5.place(x=550,y=900)



root.geometry("1000x1000")
root.mainloop()