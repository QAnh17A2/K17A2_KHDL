# Nhập hai số tự nhiên m và n từ bàn phím
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (m < n): "))

# Kiểm tra điều kiện m < n
if m >= n:
    print("Vui lòng nhập lại sao cho m < n.")
else:
    # In ra các số chia hết cho m trong khoảng từ 1 đến n
    print(f"Các số chia hết cho {m} trong khoảng từ 1 đến {n} là:")
    for i in range(1, n + 1):
        if i % m == 0:
            print(i)
            
