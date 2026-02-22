import threading
import time

def download_file(filename, delay):
    print(f"[Thread] กำลังดาวน์โหลด {filename}...")
    time.sleep(delay)  # จำลองเวลาที่ใช้โหลดไฟล์ (I/O)
    print(f"[Thread] โหลด {filename} เสร็จสิ้น!")

if __name__ == "__main__":
    start_time = time.time()
    
    # สร้าง Thread สำหรับงานแต่ละชิ้น
    t1 = threading.Thread(target=download_file, args=("วิดีโอ A.mp4", 2))
    t2 = threading.Thread(target=download_file, args=("วิดีโอ B.mp4", 2))
    t3 = threading.Thread(target=download_file, args=("วิดีโอ C.mp4", 2))

    # สั่งให้เริ่มทำงานพร้อมกัน
    t1.start()
    t2.start()
    t3.start()

    # รอให้ทุก Thread ทำงานเสร็จก่อนไปบรรทัดต่อไป
    t1.join()
    t2.join()
    t3.join()

    print(f"ใช้เวลาทั้งหมด: {time.time() - start_time:.2f} วินาที")