# เงื่อนไขพื้นฐาน

total = 30

if total > 30 :
    print("pass")
elif total > 20 :
    print("Good")
else:
    print("Fail")


age = 19
licence = True

if age >= 18 and licence :
    print("You can drive a car")
elif age >=18 and not licence :
    print("you need to get a drive licence first")
else :
    print("you can not drive a car")


#การใช้ If else แบบช้อนกัน ์ำหำก รด

score = 90

if score > 60 :
    if score > 80 :
        print("Grade A")
    elif score > 70 :
        print("Grade B")
else :
    print("Fail")

#การเขียนเปรียบเทียบเงื่อนไขแบบลดรูป
# Ternary oneline if else

age = 1
status = "บรรลุนิติภาวะ" if age >=18 else "ยังไม่บรรลุนิติภาวะ"
print(f"Status : {status}")

#เปรียบเทียบข้อความ
password="123qwe"
if password == "123qwe" :
    print("Access complete")
else : 
    print("Access Fail")