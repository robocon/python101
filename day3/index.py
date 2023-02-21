from tkinter import *
from tkinter import ttk
from tkinter import messagebox

gui = Tk()
gui.title('โปรแกรมบันทึกหวย')
gui.geometry('800x600')

l1 = Label(gui,text='โปรแกรมบันทึกหวย', font=('MesloLGM NF', 18), fg='#1f1f1f')
l1.place(x=0,y=0)

gui.mainloop()