class Patient:
    myname = ''
    def __init__(self, name,age):
        Patient.myname = name
        self.age = int(age)
        
    def checkAge(self):
        if(self.age < 20):
            print('การคำนวณ BMI เหมาะกับผู้ที่มีอายุ 20ปีขึ้นไป')
            return 1
        
class TestBmi(Patient):
    resBmi = 0
    def __init__(self, weight, height):
        self.weight = int(weight)
        self.height = int(height)/100
        
    def calculate(self):
        self.resBmi = self.weight/(self.height**2)
    
    def findBmi(self):
        self.calculate()
        if(self.resBmi < 18.5):
            bmiTxt = 'อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม'
        elif (self.resBmi >= 18.5 and self.resBmi < 23) :
            bmiTxt = 'อยู่ในเกณฑ์ปกติ'
        elif (self.resBmi >= 23 and self.resBmi < 25) :
            bmiTxt = 'น้ำหนักเกิน'
        elif (self.resBmi >= 25 and self.resBmi < 29) :
            bmiTxt = 'โรคอ้วนระดับที่1'
        elif (self.resBmi > 29) :
            bmiTxt = 'โรคอ้วนระดับที่2'
        return bmiTxt

    def display(self):
        bmiTxt = self.findBmi()
        print(f'\nค่า BMI ของคุณ {Patient.myname} อยู่ที่ {self.resBmi:,.2f} แปรผลได้คือ {bmiTxt} \n')
        print('ข้อมูลจาก เว็ปไซต์คณะแพทย์ศาสตร์ศิริราชพยาบาล: https://www.si.mahidol.ac.th/th/healthdetail.asp?aid=1361 \n')

class TestHypertension(Patient):
    def __init__(self, sys, dia):
        self.sys = int(sys)
        self.dia = int(dia)
        
    def calHypertension(self):
        if self.sys<120 and self.dia<80 :
            txt = 'ความดันโลหิตที่ดี'
        elif ( self.sys>=120 and self.sys<=129 ) or (self.dia>=80 and self.dia<=84) :
            txt = 'ความดันโลหิตปกติ'
        elif ( self.sys>=130 and self.sys<=139 ) or (self.dia>=85 and self.dia<=89) :
            txt = 'ความดันโลหิตค่อนข้างสูง'
        elif ( self.sys>=140 and self.sys<=159 ) or (self.dia>=90 and self.dia<=99) :
            txt = 'ความดันโลหิตสูงเล็กน้อย (ระยะที่ 1)'
        elif ( self.sys>=160 and self.sys<=179 ) or (self.dia>=100 and self.dia<=109) :
            txt = 'ความดันโลหิตสูงปานกลาง (ระยะที่ 2)'
        elif self.sys>=130 or self.dia>=110 :
            txt = 'ความดันโลหิตสูงมาก (ระยะที่ 3)'
        return txt
    
    def display(self):
        txt = self.calHypertension()
        print(f'\nค่าความดันโลหิตของคุณ {Patient.myname} คือ {self.sys}/{self.dia} แปรผลได้คือ {txt}\n')
    
while True:
    print('1. คำนวณ BMI')
    print('2. หาค่าความดันโลหิต')
    
    p=input('เลือกเมนูที่ต้องการใช้งาน:')
    if int(p)==1:
        name = input('คุณชื่ออะไร:')
        age = input('อายุเท่าไร:')
        p = Patient(name, age)
        ca = p.checkAge()
        if(ca==1):
            exit(1)
            
        else:
            weight = input('น้ำหนักเท่าไร:')
            height= input('ส่วนสูงเท่าไร:')
            tc = TestBmi(weight, height)
            tc.display()
        
    elif int(p)==2:
        name = input('คุณชื่ออะไร:')
        sys = input('ความดันตัวบน (Systolic):')
        dia= input('ความดันตัวล่าง (Diastolic):')
        hp = TestHypertension(sys,dia)
        hp.display()
    