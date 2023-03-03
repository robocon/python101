from dotenv import dotenv_values
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

winWidth=400
winHeight=300

gui = Tk()
gui.title('โปรแกรมตรวจสอบระดับความดันในเส้นเลือด')
gui.geometry(str(winWidth)+"x"+str(winHeight))
gui.maxsize(winWidth,winHeight)

def calHypertension(sys, dia):
    if sys<120 and dia<80 :
        txt = 'ความดันโลหิตที่ดี'
        showLabel.configure(foreground='green')

    elif ( sys>=120 and sys<=129 ) or (dia>=80 and dia<=84) :
        txt = 'ความดันโลหิตปกติ'
        showLabel.configure(foreground='green')

    elif ( sys>=130 and sys<=139 ) or (dia>=85 and dia<=89) :
        txt = 'ความดันโลหิตค่อนข้างสูง'
        showLabel.configure(foreground='orange')

    elif ( sys>=140 and sys<=159 ) or (dia>=90 and dia<=99) :
        txt = 'ความดันโลหิตสูงเล็กน้อย (ระยะที่ 1)'
        showLabel.configure(foreground='orange')

    elif ( sys>=160 and sys<=179 ) or (dia>=100 and dia<=109) :
        txt = 'ความดันโลหิตสูงปานกลาง (ระยะที่ 2)'
        showLabel.configure(foreground='red')

    elif sys>=130 or dia>=110 :
        txt = 'ความดันโลหิตสูงมาก (ระยะที่ 3)'
        showLabel.configure(foreground='red')

    return txt


def submitForm():
    if numSys.get().strip()=='' or numDia.get().strip()=='':
        messagebox.showinfo('ข้อมูลไม่ครบ','กรุณาใส่ค่าความดันให้ครบถ้วน')
        
    sys = int(numSys.get())
    dia = int(numDia.get())

    today = datetime.now()

    txt=calHypertension(sys, dia)
    defaultMsg.set(txt)

    config = dotenv_values('.env')

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(config['FIREBASE_ADMINSDK'])

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': config['FRIEBASE_DB_URL']
    }) 

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference('/hypertension')
    ref.push({
        'date':today.isoformat(),
        'sys':sys,
        'dia':dia,
        'text':txt
    })

    numSys.delete(0, END)
    numDia.delete(0, END)

defaultMsg = StringVar()

lbSys = ttk.Label(gui, text="ความดันตัวบน (Systolic):", font=('TH Sarabun New', 16))
lbSys.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

numSys = ttk.Entry(gui)
numSys.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

lbDia = ttk.Label(gui, text="ความดันตัวล่าง (Diastolic):", font=('TH Sarabun New', 16))
lbDia.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

numDia = ttk.Entry(gui)
numDia.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

save_button = ttk.Button(gui, text="ตรวจสอบ",command=submitForm)
save_button.grid(column=0, row=2, padx=5, pady=5, columnspan=2)

showLabel = ttk.Label(gui, textvariable=defaultMsg, font=('TH Sarabun New', 16, 'bold'))
showLabel.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5, columnspan=2)

gui.mainloop()