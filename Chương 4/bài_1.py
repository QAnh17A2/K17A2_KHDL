# Nhập một số từ bàn phím
num = float(input("Nhập một số: "))

# Kiểm tra xem số đó có phải là số dương hay không
if num > 0:
    # Tính bình phương của số và in ra
    binh_phuong = num ** 2
    print(f"Bình phương của {num} là {binh_phuong}")
else:
    print("Số không phải là số dương.")
