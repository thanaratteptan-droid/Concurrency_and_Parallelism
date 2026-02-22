import concurrent.futures
import time

def count_primes(n):
    print(f"[Process] กำลังคำนวณหาจำนวนเฉพาะตั้งแต่ 1 ถึง {n}...")
    count = 0
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    print(f"[Process] เจอจำนวนเฉพาะ {count} ตัว ในช่วง 1 ถึง {n}")
    return count

if __name__ == "__main__":
    start_time = time.time()
    numbers = [1000000, 2000000, 3000000] # ตัวเลขขนาดใหญ่เพื่อให้ CPU คำนวณหนัก

    # แบ่งงานให้ CPU แต่ละคอร์ช่วยกันคิด
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(count_primes, numbers))

    print(f"ใช้เวลาทั้งหมด: {time.time() - start_time:.2f} วินาที")