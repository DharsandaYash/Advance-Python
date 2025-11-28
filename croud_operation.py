from tkinter import *
import sqlite3 as sq
from tkinter import messagebox,ttk
def init_db():
    conn = sq.connect("my.db")
    cursor = conn.cursor()
    cursor.execute(""" 
    CREATE TABLE if not exists  Product_Items(id integer primary key autoincrement,
                                name text,
                                price integer)""")
    cursor.close()
    conn.close()
init_db()
root=Tk()
gp1=LabelFrame(root,text="For Record Insert",width=500,height=200)
gp1.pack(padx=20,pady=20,fill="x",expand=False)

lbl1=Label(gp1,text="Name")
lbl1.place(x=20,y=30)
e1=Entry(gp1)
e1.place(x=90,y=30)

lbl2=Label(gp1,text="Price")
lbl2.place(x=20,y=80)
e2=Entry(gp1)
e2.place(x=90,y=80)

def Save_Records():
    nm = e1.get()
    pr = e2.get()
    #print(nm)
    #print(pr)
    e1.focus()
    if(nm=="" and pr == ""):
        messagebox.showinfo("Error","Please input some values")
    else:
        conn = sq.connect("my.db")
        cursor = conn.cursor();
        cursor.execute("insert into Product_Items(name,price)values(?,?)",(nm,pr))
        conn.commit()
        cursor.close()
        conn.close()
        tree.insert("",0,values=(cursor.lastrowid,nm,pr))
        e1.delete(0,END)
        e2.delete(0,END) 
        #for i in tree.get_children():
        #     tree.delete(i)
        #e1.insert(END,"")
        #Show_Records()
           
btn1 = Button(gp1,text="Save",command=Save_Records)
btn1.place(x=90,y=120) 

gp2=LabelFrame(root,text="Show Information",width=500,height=200)
gp2.pack(padx=20,pady=20,fill="x",expand=False)

tree = ttk.Treeview(gp2,columns=("id","name","price"),show="headings")
tree.heading("id",text="Product ID")
tree.heading("name",text="NAme")
tree.heading("price",text="PRice")
tree.column(column=0,width=60,anchor="center")
tree.column(column=1,width=100,anchor="center")
tree.column(column=2,width=100,anchor="center")
tree.pack(padx=10,pady=10,fill="both",expand=False)

def Show_Records():
    conn = sq.connect("my.db")
    cursor = conn.cursor();
    cursor.execute("select * from Product_Items")
    rows=cursor.fetchall()
    for row in rows:
        #tree.insert("",0,values=row)
        tree.insert(parent="",index="end",values=row)
    cursor.close()
    conn.close()
Show_Records()

gp3=LabelFrame(root,text="Operation Info",width=500,height=100)
gp3.pack(padx=20,pady=20,fill="both",expand=False)

def delete_record():
    get_id = tree.item(tree.focus())
    if(get_id["values"]==""):
        messagebox.showwarning("Warning","Select Record")   
    else:
        record_id = get_id["values"][0]
        conn = sq.connect("my.db")
        cursor = conn.cursor();
        cursor.execute("delete from Product_Items where id=?",(record_id,))
        conn.commit()
        cursor.close()
        conn.close()
        tree.delete(tree.focus())
  

btn2 = Button(gp3,text="Delete",command=delete_record)
btn2.place(x=30,y=10)

def update_record():
    row = tree.item(tree.focus())
    if(row["values"] == ""):
        messagebox.showwarning("Warning","Select Record")
        return 
    else:
        id1 = row["values"][0]
        nm1 = row["values"][1]
        pr1 = row["values"][2]
        
        top = Toplevel(root)
        top.geometry("300x300")
        
        l1 = Label(top,text="Name")
        l1.place(x=20,y=30)
        entry1 = Entry(top)
        entry1.place(x=80,y=30)

        l2 = Label(top,text="Price")
        l2.place(x=20,y=80)
        entry2 = Entry(top)
        entry2.place(x=80,y=80)

        entry1.insert(0,nm1)
        entry2.insert(0,pr1)

        def rec_update():
            nm2 = entry1.get()
            pr2 = entry2.get()
            conn = sq.connect("my.db")
            cursor = conn.cursor();
            cursor.execute("update Product_Items set name=?,price=? where id=?",(nm2,pr2,id1))
            conn.commit()
            cursor.close()
            conn.close()
            tree.item(tree.focus(),values=(id1,nm2,pr2))
        btn4 = Button(top,text="Update",command=rec_update)
        btn4.place(x=80,y=150)


        top.mainloop()
btn3 = Button(gp3,text="Edit",command=update_record)
btn3.place(x=100,y=10)


root.geometry("500x730+100+20")
root.mainloop()
