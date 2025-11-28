from tkinter import *;
from tkinter import messagebox;
from tkinter import ttk;
import sqlite3 as sq;
import csv 

root = Tk();
root.title("SC");
data = "";

def init():
    cnn = sq.connect("MY.db");
    cursor = cnn.cursor();
    cursor.execute("create table if not exists list_record(id integer primary key autoincrement,name text,subject text)")
    cursor.close();
    cnn.close();
init();


def insert_data():
    listb = txt1.get(txt1.curselection())
    nm = txt2.get()
    a=len(txt2.get());
    b = len(listb);
    if(a>0 and b>0):
        cnn = sq.connect("MY.db");
        cursor = cnn.cursor();
        cursor.execute("insert into list_record(name,subject)values(?,?)",(nm,listb));
        txt1.delete(0,END);
        txt2.delete(0,END);
        txt1.focus();
        cnn.commit();
        cursor.close();
        cnn.close();
        messagebox.showinfo("Information","Data Inserted !")
        data.insert("",END,values=(cursor.lastrowid,nm,listb));
    else:
        messagebox.showinfo("Information","Please Fill Data")
    


gp1 = LabelFrame(root,text="Insert Records",width="400",height="200")
gp1.pack(padx=150,pady=10,fill="x",expand=False);


gp3 = LabelFrame(root,text="All Records",width="200",height="500")
gp3.pack(padx=350,pady=10,fill="both",expand=False);

def display():
    cnn = sq.connect("MY.db");
    cursor = cnn.cursor();
    cursor.execute("select * from list_record"); 
    rows = cursor.fetchall();
    global data 
    data = ttk.Treeview(gp3,columns=["id","name","subject"], show="headings")
    data.heading("id",text="id")
    data.heading("name",text="name")
    data.heading("subject",text="subject")
    for row in rows:
        data.insert("",END,values=row)
    data.pack(expand=True,fill="both", padx=10, pady=10)
    cursor.close();
    cnn.close()
display();

lbl1 = Label(gp1,text="Subject");
lbl1.place(x=30,y=35);
txt1 = Listbox(gp1,height=5);
txt1.insert(END,"BCA")
txt1.insert(END,"B.COM")
txt1.insert(END,"BBA")
txt1.insert(END,"MCA")
txt1.insert(END,"M.COM")
txt1.place(x=120,y=35);

lbl2 = Label(gp1,text="Feculty Name");
lbl2.place(x=30,y=10);
txt2 = Entry(gp1);
txt2.place(x=120,y=10)


btn1 = Button(gp1,text="Save Data",command=insert_data);
btn1.place(x=80,y=130);


root.geometry("1000x600");
root.mainloop()