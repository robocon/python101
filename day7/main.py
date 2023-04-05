import tkinter as tk
import ttkbootstrap as ttk
import requests as req
import json as json
from datetime import datetime
from dotenv import dotenv_values
from ttkbootstrap.constants import *
from tkinter import * 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

config = dotenv_values('.env')

# Fetch the service account key JSON file contents
cred = credentials.Certificate(config['FIREBASE_ADMINSDK'])

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': config['FRIEBASE_DB_URL']
}) 


def copyText():
    shortInput.select_range(0,'end')
    shortInput.event_generate("<<Copy>>")
    
def doShortUrl():
    global config
    
    today = datetime.now()
    myobj={
        "url": longInput.get().strip(),
        "domain": "tinyurl.com"
    }
    headers = {"Authorization": config['TINYTOKEN']}
    
    x = req.post(config['TINYHOST']+"/create", json=myobj, headers=headers)
    y = json.loads(x.text)
    shortInput.delete(0, END)
    shortInput.insert(0, y["data"]["tiny_url"])
    
    ref = db.reference('/myShortUrl')
    ref.push({
        'date':today.isoformat(),
        'longurl':longInput.get().strip(),
        'shorturl':y["data"]["tiny_url"]
    })
    
    
root = tk.Tk()
root.title('โปรแกรมสร้าง URL แบบสั้น')

lb0 = ttk.Label(root, text="URL shortener", font=('TH Sarabun New', 16))
lb0.grid(column=0, row=0, padx=5, pady=5, columnspan=3)

lb1 = ttk.Label(root, text="Long URL: ", font=('TH Sarabun New', 16))
lb1.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

longInput = ttk.Entry(root)
longInput.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

b1 = ttk.Button(root, text="Shorten URL", bootstyle=SUCCESS, command=doShortUrl)
b1.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

lb2 = ttk.Label(root, text="Short URL: ", font=('TH Sarabun New', 16))
lb2.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

#state="readonly",
shortInput = ttk.Entry(bootstyle="info")
shortInput.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

b2 = ttk.Button(root, text="COPY", bootstyle=INFO, command=copyText)
b2.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)



tree = ttk.Treeview(root, show='headings')

tree['columns'] = ('first_name', 'last_name', 'email')

tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

tree.insert(parent='', index='end', iid=0, text="Parent", values=("John","Wick","mail.com"))

tree.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5, columnspan=3)

root.mainloop()