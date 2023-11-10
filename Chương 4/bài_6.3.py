# Nhập hai số a, b
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

# Thuật toán Euclid để tìm UCLN
while b != 0:
    a, b = b, a % b

print(f"Ước số chung lớn nhất là {a}")
