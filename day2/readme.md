# เริ่มใช้งาน tkinter
ไม่รอช้าอะไรแล้ว ลุยกันเล๊ยยยยยยยยยย
```
from tkinter import *
from tkinter import ttk

gui = Tk()
gui.title('โปรแกรมบันทึกข้อมูล')
gui.geometry('500x400')
```
การเรียกใช้งานหลักๆ ก็จะหน้าตาประมาณนี้<br><br>

# Label
```
l1 = Label(gui,text='โปรแกรมบันทึกหวย', font=('TH SarabunPSK', 30), fg='#1f1f1f')
l1.place(x=0,y=0)
```
```text=``` ข้อความที่แสดงใน label<br>
```font=``` จะให้แสดงเป็นฟอนต์แบบไหน<br>
```fg=``` ใส่สี<br>
```.place(x,y)``` เป็นการกำหนดว่าจะให้แสดงในแกน X,Y ตรงไหน<br><br>

# Button
```
def Button2():
    text = "Hello Text Button"
    messagebox.showinfo('Title info', text)
    
fb2 = Frame(gui)
fb2.place(x=0,y=100)
b2 = ttk.Button(fb2, text='Test Button', command=Button2)
b2.pack(ipadx=5,ipady=5)
```
เริ่มจากกำหนดเฟรมให้ปุ่มก่อนด้วย ```Frame()``` กับ ```.place(x,y)``` จากนั้นสร้างปุ่มด้วย ```.Button(fb2,text='xxx',command=Button2)``` ซึ่งจะเป็นการโยนค่า ```fb2``` ที่เรากำหนดจาก ```Frame()``` เข้าไปในปุ่มอีกทีหนึ่ง<br><br>
```command=``` เป็นการกำหนดคำสั่งที่เกิดขึ้นเมื่อเราคลิกปุ่มจะให้ทำอะไร ในที่นี้คือให้มันทำงานในฟังก์ชั่น ```Button2()```
```.pack(ipadx=xxx,ipady=xxx)``` ค่า ```ipadx,ipady``` ก็เหมือนกับทำ padding ใน css นั่นเอง
