# asyncio-demo
# Asyncio Example

## รายละเอียดโปรแกรม
โปรแกรมนี้ใช้ `asyncio` เพื่อรันหลาย task พร้อมกัน โดยแต่ละ task มีเวลาการทำงานที่แตกต่างกัน

## วิธีใช้งาน
1. ติดตั้ง Python 3.7+ ขึ้นไป
2. เปิด Terminal หรือ Command Prompt และรันคำสั่ง
   python script.py



## ตัวอย่างผลลัพธ์จากการัน
- Task A started
- Task B started
- Task C started
- Task C completed after 1 seconds
- Task A completed after 2 seconds
- Task B completed after 3 seconds
- All tasks completed: ['Result from A', 'Result from B', 'Result from C']
- Total execution time: 3.0 seconds
## สังเกต: โปรแกรมใช้เวลาเพียง 3 วินาที (เร็วกว่า 2 + 3 + 1 = 6 วินาที ถ้ารันทีละตัว)