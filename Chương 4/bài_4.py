# Nhập ba số từ bàn phím
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

# Tìm số lớn nhất
so_lon_nhat = max(num1, num2, num3)

# In ra số lớn nhất
print(f"Số lớn nhất trong ba số là: {so_lon_nhat}")
