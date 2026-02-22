import asyncio
import time

async def fetch_user_data(user_id):
    print(f"[Async] กำลังขอข้อมูล User ID: {user_id}...")
    await asyncio.sleep(1)  # จำลองการรอเซิร์ฟเวอร์ตอบกลับ (Non-blocking I/O)
    print(f"[Async] ได้รับข้อมูล User ID: {user_id} แล้ว")
    return f"Data_{user_id}"

async def main():
    start_time = time.time()
    
    # สร้าง Task รันฟังก์ชันพร้อมกัน 5 ตัว
    tasks = [fetch_user_data(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    
    print(f"ผลลัพธ์ที่ได้: {results}")
    print(f"ใช้เวลาทั้งหมด: {time.time() - start_time:.2f} วินาที")

if __name__ == "__main__":
    asyncio.run(main())