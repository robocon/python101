# EP.5 

แนะนำการใช้งาน pip โมดูลจัดการแพ็คเกจเสริมเพื่อติดตั้งแพ็คเกจ/ไลบรารีจากภายนอก

[x] การใช้งาน pip
```
>pip install unclechat
```

[x] ปัญหาที่มักเกิดบ่อยกับ pip 

แก้ปัญหาโดยการยิงพาธเต็มไปเลย
```
>"PATH_TO_PYTHON" -m pip install unclechat
```

### เทคนิคเล็กๆน้อยๆ เกี่ยวกับ List
```
# เกี่ยวกับการเพิ่มลบข้อมูล
friend = ['somchai', 'somsak', 'somsri']

friend.append('sompong')
>['somchai', 'somsak', 'somsri', 'sompong']

friend.remove('somsak')
>['somchai', 'somsri']

del friend[0]
>['somsak', 'somsri']

del friend[-1]
>['somchai', 'somsak']
```

### basic for 
```
friend = ['somchai', 'somsak', 'somsri']

for f in friends:
    print(f)

>somchai
>somsak
>somsri
```

### Dictionary
เหมือนเดิมนะ ในมุมของ php คือ key-value นั่นล่ะ
```
friends = {'somchai':'0851111111', 'somsak':'0892222222', 'somsri':'0863333333'}

# items() คือเปลี่ยนให้เป็น tuple ทำให้ key-value ออกมาพร้อมกัน
for f in friends.items():
    print(f)
>('somchai':'0851111111')
>('somsak':'0892222222')
>('somsri':'0863333333')

# ออกมาเฉพาะ value
friends.values()

# ออกมาเฉพาะ key
friends.keys()
```