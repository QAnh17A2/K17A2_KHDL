# Nhập hệ số a, b
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

# Giải phương trình
if a == 0:
    print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Nghiệm x: {x}")
