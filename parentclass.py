from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
from tkinter import ttk

root=Tk()
root.title("hello")
def init():
    con=sq.connect("my1.db")
    cur=con.cursor()
    cur.execute("""create table if not exists product(id integer primary key autoincrement,name text,price real,catagary text)""")
    cur.close()
    con.close()
init()

def insert():
    con=sq.connect("my1.db")
    cur=con.cursor()
    cur.executemany("""
        INSERT INTO product (name, price, catagary)
        VALUES (?, ?, ?)
        """, [
        ('Laptop', 55000.00, 'Electronics'),
        ('Mobile Phone', 25000.00, 'Electronics'),
        ('Chair', 3500.00, 'Furniture'),
        ('Table', 5000.00, 'Furniture'),
        ('Book', 400.00, 'Stationery')
    ])
    con.commit()
    cur.close()
    con.close()



lb2=LabelFrame(root,text="View Record",height=200,width=600)
lb2.pack(fill="both")

tree=ttk.Treeview(lb2,columns=("id","price","catagary"),height=50)

tree.heading("#0", text="Product Name", anchor=W)
tree.heading("id",text="ID")

tree.heading("price",text="Price")
tree.heading("catagary",text="CATAGORY")

tree.column("#0", width=150, anchor=W)


p1=tree.insert("",END,text="Electronics",open=True)  
p2=tree.insert("",END,text="Furniture",open=True)  



def viewrecord():
    con=sq.connect("my1.db")
    cur=con.cursor()
    cur.execute("select * from product where catagary=?",("Electronics",))
    perent1=cur.fetchall()

    for row in perent1:
        tree.insert(p1,END,text=row[1],values=[row[0],row[2],row[3]])
    
    cur.execute("select * from product where catagary=?",("Furniture",))
    perent2=cur.fetchall()
    for row in perent2:
        tree.insert(p2,END,text=row[1],values=[row[0],row[2],row[3]])
    
    con.commit()
    cur.close()
    con.close()
viewrecord()

tree.pack(fill="both")
root.geometry("1000x1000")
root.mainloop()