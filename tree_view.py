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
    cursor.execute("create table if not exists My_Record(id integer primary key autoincrement,name text,price integer)")
    cursor.close();
    cnn.close();
init();

nm = StringVar();
pr = IntVar();
def insert_data():
    name = nm.get();
    price = pr.get()
    a=len(name);
    b = len(txt2.get());
    if(a>0 and b>0):
        cnn = sq.connect("MY.db");
        cursor = cnn.cursor();
        cursor.execute("insert into My_Record(name,price)values(?,?)",(name,price));
        txt1.delete(0,END);
        txt2.delete(0,END);
        txt1.focus();
        cnn.commit();
        cursor.close();
        cnn.close();
        messagebox.showinfo("Information","Data Inserted !")
        for widget in gp3.winfo_children():
            widget.destroy()
        display();
    else:
        messagebox.showinfo("Information","Please Fill Data")
se = StringVar()
def search_data(event):
    for widget in gp3.winfo_children():
        widget.destroy()
    search = se.get();
    if(search==""):
        display();
    else:
        cnn = sq.connect("MY.db");
        cursor = cnn.cursor();
        cursor.execute("SELECT * FROM My_Record WHERE id LIKE ? or name LIKE ? or price LIKE ?",(f"%{search}%", f"%{search}%", f"%{search}%"));
        rows = cursor.fetchall();
        global data;
        data = ttk.Treeview(gp3,columns=["id","name","price"], show="headings")
        data.heading("id",text="id")
        data.heading("name",text="name")
        data.heading("price",text="price")
        for row in rows:
            data.insert("",END,values=row)
        data.pack(expand=True,fill="both", padx=10, pady=10)
        cnn.commit();
        cursor.close();
        cnn.close();

def delete_data():
    global data;
    d = data.selection();
    a = len(d)
    if(a>0):
        msg = messagebox.askyesno("Qustion","Do You Want To Delete This Record ?")
        if(msg):
            v = data.item(d[0])["values"];
            v1 = v[0];
            cnn = sq.connect("MY.db");
            cursor = cnn.cursor();
            cursor.execute("delete from My_Record where id=(?)",(v1,));
            cnn.commit();
            cursor.close()
            cnn.close();
            messagebox.showinfo("Information","Record Deleted !");
    else:
        messagebox.showinfo("Information","Select Record !");
    for widget in gp3.winfo_children():
        widget.destroy()
    display();

def update_data():
    root2=Toplevel(root);
    root2.title("Update Frame");

    nm = StringVar();
    pr = IntVar();
    gp4 = LabelFrame(root2,text="Update Data",width="200",height="300")
    gp4.pack(padx=350,pady=10,fill="both",expand=False);

    lbl4 = Label(gp4,text="Name");
    lbl4.place(x=20,y=30);
    txt4 = Entry(gp4,textvariable=nm);
    txt4.place(x=80,y=30);
    
    global data;
    d = data.selection();
    a = len(d)
    if (a>0):
        v = data.item(d[0])["values"];
        txt4.insert(0,v[1])

        lbl5 = Label(gp4,text="Price");
        lbl5.place(x=20,y=90);
        txt5 = Entry(gp4,textvariable=pr);
        txt5.place(x=80,y=90);
        txt5.insert(0,v[2])

        def up_data():
            name = nm.get();
            price = pr.get();
            cnn = sq.connect("MY.db");
            cursor = cnn.cursor();
            cursor.execute("update My_Record set name=(?),price=(?) where id=(?)",(name,price,v[0]));
            cnn.commit();
            messagebox.showinfo("Information","Record Updated !")
            cursor.close();
            cnn.close();
            for widget in gp3.winfo_children():
                widget.destroy()
            display();

        btn5 = Button(gp4,text="Update & Save",command=up_data);
        btn5.place(x=80,y=130)

        root2.geometry("1000x400+100+200");
        root2.mainloop();
    else:
        messagebox.showinfo("Information","Select Data !")

def export_data():
    cnn = sq.connect("MY.db");
    cursor = cnn.cursor();
    cursor.execute("select * from My_Record"); 
    data = cursor.fetchall();
    f = open("my_data.csv","w",newline="")
    writer = csv.writer(f)
    writer.writerow(["id","name","price"])
    writer.writerows(data)
    messagebox.showinfo("Information","Export Complete")

gp1 = LabelFrame(root,text="Insert Records",width="400",height="200")
gp1.pack(padx=150,pady=10,fill="x",expand=False);

gp2 = LabelFrame(root,text="Search Records",width="400",height="200")
gp2.pack(padx=150,pady=10,fill="x",expand=False);

gp3 = LabelFrame(root,text="All Records",width="200",height="500")
gp3.pack(padx=350,pady=10,fill="both",expand=False);

def display():
    cnn = sq.connect("MY.db");
    cursor = cnn.cursor();
    cursor.execute("select * from My_Record"); 
    rows = cursor.fetchall();
    global data 
    data = ttk.Treeview(gp3,columns=["id","name","price"], show="headings")
    data.heading("id",text="id")
    data.heading("name",text="name")
    data.heading("price",text="price")
    for row in rows:
        data.insert("",END,values=row)
    data.pack(expand=True,fill="both", padx=10, pady=10)
    cursor.close();
    cnn.close()
display();

lbl1 = Label(gp1,text="Name");
lbl1.place(x=30,y=50);
txt1 = Entry(gp1,textvariable=nm);
txt1.place(x=80,y=50);

lbl2 = Label(gp1,text="Price");
lbl2.place(x=30,y=90);
txt2 = Entry(gp1,textvariable=pr);
txt2.place(x=80,y=90)

lbl3 = Label(gp2,text="Enter Something")
lbl3.place(x=30,y=50)
txt3 = Entry(gp2,textvariable=se);
txt3.place(x=150,y=50);
txt3.bind("<KeyRelease>", search_data)

btn1 = Button(gp1,text="Save Data",command=insert_data);
btn1.place(x=80,y=130);
btn2 = Button(gp2,text="Search",command=search_data(event="<KeyRelease>"));
btn2.place(x=120,y=90)
btn4 = Button(root,text="Update",command=update_data);
btn4.pack();
btn3 = Button(root,text="Delete",command=delete_data);
btn3.pack();
btn5 = Button(root,text="Export",command=export_data);
btn5.pack();

root.geometry("1000x600");
root.mainloop()