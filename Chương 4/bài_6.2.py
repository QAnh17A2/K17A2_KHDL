# Nhập tháng và năm
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra hợp lệ
if thang < 1 or thang > 12 or nam < 0:
    print("Không hợp lệ")
else:
    if thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            print("Tháng 2 có 29 ngày")
        else:
            print("Tháng 2 có 28 ngày")
    elif thang in [1, 3, 5, 7, 8, 10, 12]:
        print(f"Tháng {thang} có 31 ngày")
    else:
        print(f"Tháng {thang} có 30 ngày")
