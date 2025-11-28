from tkinter import *;
from tkinter import filedialog;
from tkinter import ttk;
import csv;
import pandas

root = Tk()
root.title("SC")

file_path = ""

def get_file():
    txt1.delete(0,END)
    global file_path
    file_path = filedialog.askopenfile(filetypes=[("CSV FILES","*.csv")]);
    txt1.insert(0,file_path.name)

def read_file():
    path = txt1.get()
    delimiter = txt2.get()
    header = cb.get()
    ecncode = txt3.get()
    df = pandas.read_csv(path,delimiter=delimiter,encoding=ecncode,header=0)
    txt.delete("1.0",END)
    txt.insert(END,df.to_string(index=False))

lbl1 = Label(root,text="CSV File")
lbl1.place(x=30,y=30)
txt1 = Entry(root,width="60")
txt1.place(x=120,y=30)
btn1 = Button(root,text="Get File",command=get_file)
btn1.place(x=520,y=28)
btn2 = Button(root,text="Read File",command=read_file)
btn2.place(x=600,y=28)

lbl2 = Label(root,text="Delimiter")
lbl2.place(x=30,y=70)
txt2 = Entry(root)
txt2.insert(0,",")
txt2.place(x=120,y=70)

lbl3 = Label(root,text="Heading")
lbl3.place(x=30,y=110)
value = StringVar(value="yes")
cb = ttk.Combobox(root,textvariable=value,values=["yes","no"])
cb.place(x=120,y=110)

lbl4 = Label(root,text="Encoding")
lbl4.place(x=30,y=150)
txt3 = Entry(root);
txt3.insert(0,"utf-8")
txt3.place(x=120,y=150)

def save_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")
    delimiter = txt2.get()
    encode = txt3.get()
    get_data = txt.get("1.0", END).strip().split("\n")

    df = pandas.DataFrame(get_data)
    df = df[0].str.split(",",expand=True)
    df.to_csv(file_path,index=False,header=False)
btn3 = Button(root,text="save file",command=save_data)
btn3.place(x=30,y=180)

gp1 = LabelFrame(root,text="CSV FILE",width=300,height=200)
gp1.place(x=30,y=220)
txt = Text(gp1);
txt.pack(padx=10,pady=10,expand=False)
root.geometry("900x700")
root.mainloop()