# Nhập chuỗi s1
s1 = input("Nhập chuỗi s1: ")

# Nhập chuỗi s2 
s2 = input("Nhập chuỗi s2: ")

# Nhập chuỗi s3 
s3 = input("Nhập chuỗi s3: ")

# Nhập chỉ mục index 
index = int(input("Nhập index: "))

# Tính chiều dài của các chuỗi
length_s1 = len(s1)
length_s2 = len(s2)
length_s3 = len(s3)

# Tạo chuỗi con s4 từ chuỗi s1
s4 = s1[index-1:]

# Lặp lại chuỗi s2: 2 lần
lap_lai_s2 = s2 * 2

# Hiển thị kết quả
print(f"Chiều dài chuỗi s1 = {length_s1}")
print(f"Chiều dài chuỗi s2 = {length_s2}")
print(f"Chiều dài chuỗi s3 = {length_s3}")
print(f"Chuỗi s4 = {s4}")
print(f"Chuỗi s2 lặp lại 2 lần = {lap_lai_s2}")
