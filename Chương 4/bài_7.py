def tinh_tong_chu_so(N):
    # Khởi tạo biến tổng
    tong = 0
    
    # Sử dụng vòng lặp để duyệt qua từng chữ số của N
    while N > 0:
        # Lấy chữ số cuối cùng của N và cộng vào tổng
        tong += N % 10
        
        # Loại bỏ chữ số cuối cùng của N
        N //= 10
    
    return tong

# Test với N = 2022
N = 2022
ket_qua = tinh_tong_chu_so(N)
print(f"Tổng các chữ số của {N} là: {ket_qua}")
