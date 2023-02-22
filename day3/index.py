import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

gui = Tk()
gui.title('เมียขี้เกียจจด')
gui.maxsize(300,300)
gui.config(bg="skyblue")

# gui.columnconfigure(0, weight=1)
# gui.columnconfigure(1, weight=1)

title_label = ttk.Label(gui, text="บันทึกโพย", font=('MesloLGM NF', 16))
title_label.grid(column=0, row=0, padx=5, pady=5, columnspan=3)

num_type_label = ttk.Label(gui, text="เล่น:", font=('MesloLGM NF', 16))
num_type_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

selected = tk.StringVar()
op1 = ttk.Radiobutton(gui, text='3ตัวบน', value='3up', variable=selected)
op1.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
op2 = ttk.Radiobutton(gui, text='3ตัวโต๊ด', value='3', variable=selected)
op2.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

op3 = ttk.Radiobutton(gui, text='2ตัวบน', value='2up', variable=selected)
op3.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
op4 = ttk.Radiobutton(gui, text='2ตัวล่าง', value='2down', variable=selected)
op4.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)


number_label = ttk.Label(gui, text="ระบุเลข:", font=('MesloLGM NF', 16))
number_label.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
number_entry = ttk.Entry(gui)
number_entry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5, columnspan=2)

save_button = ttk.Button(gui, text="บันทึกโพย")
save_button.grid(column=0, row=4, padx=5, pady=5, columnspan=3)

gui.mainloop()