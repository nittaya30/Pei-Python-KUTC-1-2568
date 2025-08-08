# ฟังก์ชันรับค่าคะแนนโดยตรวจสอบเงื่อนไข
def get_score(prompt, max_score):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= max_score:
                return score
            else:
                print(f"คะแนนต้องอยู่ในช่วง 0 ถึง {max_score} เท่านั้น กรุณากรอกใหม่")
        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น")

# รับค่าคะแนน
midterm = get_score("กรอกคะแนนกลางภาค (เต็ม 30): ", 30)
final = get_score("กรอกคะแนนปลายภาค (เต็ม 70): ", 70)

# คำนวณผลรวม
total = midterm + final

# แสดงผลลัพธ์
print(f"คะแนนรวมคือ: {total}")
if total >= 70:
    print("ผลการสอบ: Pass")
else:
    print("ผลการสอบ: Fail")
