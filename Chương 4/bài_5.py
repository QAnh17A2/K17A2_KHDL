# Hàm tính Ước số chung lớn nhất
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

# Hàm tính Bội số chung nhỏ nhất
def bcnn(a, b):
    return (a * b) // ucln(a, b)

# Nhập hai số từ bàn phím
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))

# Tính và in ra BCNN của hai số
ket_qua_bcnn = bcnn(so1, so2)
print(f"BCNN của {so1} và {so2} là: {ket_qua_bcnn}")
