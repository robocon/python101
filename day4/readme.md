# EP.4
[x] ทำความเข้าใจคอนเซปต์การบันทึกข้อมูลและอ่านข้อมูล

[x] การเก็บข้อมูลใน list เบื้องต้น

[x] dictionary เบื้องต้น

[x] บันทึกข้อมูลลงไฟล์ csv

[ ] การใช้งาน pip

[ ] ปัญหาที่มักเกิดขึ้นบ่อยกับ pip

# เรื่องของ List
> list ก็เหมือนกับ array ใน php ง่ายๆแบบนี้ล่ะ

### ตัวอย่าง

```
bike = ['trek', 'redline', 'treak']
```

# เรื่องของ Dictionary
> คิดซะว่าเป็น key : value ก็แล้วกัน ง่ายดี 

### ตัวอย่าง

```
brand={'car':['toyota','honda','tesla'],'color':['red','blue','green']}
```

# เปิด/บันทึก ไฟล์ csv
```
import csv

# อ่านไฟล์
with open('file_path', 'r', encoding='UTF8') as file:
    fr = csv.reader(file)
    data = list(fr)

# เขียนไฟล์
with open('file_path', 'a', encoding='UTF8') as file:
    fw = csv.writer(file)
    data ['one','two']
    fw.writerow(data)

```
mode:OpenTextMode มีค่า default เป็น "r" คือการอ่าน

เป็น "a" คือเปิดไฟล์เพื่อเขียนต่อท้าย อะไรแบบนี้เป็นต้น