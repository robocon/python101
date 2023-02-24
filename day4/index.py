import tkinter as tk
import csv
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date

fileName = 'db.csv'

""" JSON """
"""[ ] submit form ====> read json and append to end of list"""
"""[ ] show data read all data """

def readCsv():
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='UTF8', newline='') as file:
            fr = csv.reader(file)
            data = list(fr)
            return data
    else:
        return []

def submitForm():
    global allItemLen
    with open(fileName, 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        data = [str(date.today()), selected.get(), number_entry.get()]
        writer.writerow(data)
        file.close()
        
        allItemLen = len(readCsv())
        messagebox.showinfo("บันทึกข้อมูลเรียบร้อย", "เล่น:"+selected.get()+"\nเลข:"+number_entry.get());
    
def loadMessage(item):
    defaultMsg.set("วันที่: "+item[0]+' เล่น: '+item[1]+' เลข: '+item[2])
    
def prevMsg():
    global defMsgNumber,allItemLen
    items = readCsv()
    testLen = allItemLen-1
    if(defMsgNumber <= testLen and defMsgNumber > 0):
        defMsgNumber = defMsgNumber-1
        loadMessage(items[defMsgNumber])
    
def nextMsg():
    global defMsgNumber,allItemLen
    items = readCsv()
    testLen = allItemLen-1
    if(defMsgNumber < testLen):
        defMsgNumber = defMsgNumber+1
        loadMessage(items[defMsgNumber])

gui = Tk()
gui.title('เมื่อเมียอยากจดหวย')
gui.maxsize(600,300)
gui.config(bg="skyblue")

title_label = ttk.Label(gui, text="วันนี้เมียจ๋าซื้อหวยอะไรไปบ้าง", font=('MesloLGM NF', 16))
title_label.grid(column=0, row=0, padx=5, pady=5, columnspan=3)

num_type_label = ttk.Label(gui, text="เล่น:", font=('MesloLGM NF', 16))
num_type_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

selected = StringVar()
op1 = ttk.Radiobutton(gui, text='3ตัวบน', value='3ตัวบน', variable=selected)
op1.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
op2 = ttk.Radiobutton(gui, text='3ตัวโต๊ด', value='3ตัวโต๊ด', variable=selected)
op2.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

op3 = ttk.Radiobutton(gui, text='2ตัวบน', value='2ตัวบน', variable=selected)
op3.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
op4 = ttk.Radiobutton(gui, text='2ตัวล่าง', value='2ตัวล่าง', variable=selected)
op4.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

v_data = StringVar()
number_label = ttk.Label(gui, text="ระบุเลข:", font=('MesloLGM NF', 16))
number_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
number_entry = ttk.Entry(gui, textvariable=v_data)
number_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5, columnspan=2)

save_button = ttk.Button(gui, text="บันทึกโพย",command=submitForm)
save_button.grid(column=0, row=4, padx=5, pady=5, columnspan=3)

defaultMsg = StringVar()

# default message
defMsgNumber = 0
items = readCsv()
allItemLen = len(items)
if(allItemLen > 0):
    
    # load default message
    print("Load default number: "+str(defMsgNumber))
    item = items[defMsgNumber]
    loadMessage(item)
    
    showLabel = ttk.Label(gui, textvariable=defaultMsg, font=('MesloLGM NF', 16))
    showLabel.grid(column=0, row=5, padx=5, pady=5, columnspan=3)
    
    leftBtn = ttk.Button(gui, text="<<",command=prevMsg)
    leftBtn.grid(column=0, row=6, padx=5, pady=5)

    rightBtn = ttk.Button(gui, text=">>",command=nextMsg)
    rightBtn.grid(column=2, row=6, padx=5, pady=5)

gui.mainloop()