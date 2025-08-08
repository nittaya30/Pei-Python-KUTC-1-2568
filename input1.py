# name = input("what your name?")
# print("Hello",name)

# age = int(input("How old are you"))
# result = 100 - age
# print(f"You will be 100 in {result}years")

# num1 = float(input("input your frist number : "))
# num2 = float(input("input your second number : "))
# total = num1 + num2
# print(f"First number :{num1} and second number : {num2} total is : {total}")


#การเก็บข้อมูลด้วยการเคาะวรรค
x,y = input("Enter your number in two value sepreatad by space : ").split()
print(f"First number {x} Second number {y}")

#แปลงหน่วยจากเมตรเป็นเซนติดมตร
length = float(input("Enter your length in meters:"))
print(f"That's{length * 100} centimeteres")