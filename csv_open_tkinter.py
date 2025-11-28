from tkinter import *
from tkinter import ttk
import csv

root=Tk()
root.geometry("500x500")
tree=ttk.Treeview(root,columns=("id","name","city"),show="headings")
tree.heading("id",text="Id")
tree.heading("name",text="Name")
tree.heading("city",text="City")

tree.column(column=0,width=30,anchor="center")
tree.column(column=1,width=100,anchor="center")
tree.column(column=2,width=150,anchor="center")
tree.pack(padx=10,pady=20,fill="both",expand=False)


with open("data.txt","w",newline="") as f:
    row=csv.writer(f)
    row.writerow(["id","name","city"])
    rows=[["1","Yash","ksd"],["2","Kunal","pipli"],["3","harsh","pipali"],["4","ravi","farangata"]]
    row.writerows(rows)
    for i in rows:
        tree.insert("",0,values=i)
        
root.mainloop()