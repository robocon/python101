from tkinter import *
from tkinter import ttk #ธีม
from tkinter import messagebox

gui = Tk()
gui.title('โปรแกรมบันทึกข้อมูล')
gui.geometry('500x400')

l1 = Label(gui,text='โปรแกรมบันทึกหวย', font=('TH SarabunPSK', 30), fg='#1f1f1f')
l1.place(x=0,y=0)

def Button1():
    text = '*375*'
    messagebox.showinfo('เจ๊นุ๊ก บารมีมหาเฮง', text)

fb1 = Frame(gui)
fb1.place(x=0,y=50)
b1 = ttk.Button(fb1, text='เจ๊นุ๊ก', command=Button1)
b1.pack(ipadx=5,ipady=5)

def Button2():
    text = "52 - 53 - 56\n59 - 759"
    messagebox.showinfo('เจ๊ฟองเบียร์', text)
    
fb2 = Frame(gui)
fb2.place(x=0,y=100)
b2 = ttk.Button(fb2, text='เจ๊ฟองเบียร์', command=Button2)
b2.pack(ipadx=5,ipady=5)

def Button3():
    text = "สามตัว 375\nตัวฟัน 5\nเลขสองตัว\n59-52-29-79-75-72"
    messagebox.showinfo('แม่น้ำหนึ่ง', text)
    
fb3 = Frame(gui)
fb3.place(x=0,y=150)
b3 = ttk.Button(fb3, text='แม่น้ำหนึ่ง', command=Button3)
b3.pack(ipadx=5,ipady=5)


gui.mainloop()