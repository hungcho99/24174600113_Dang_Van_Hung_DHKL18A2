
# 7. Viết chương trình giải hệ phương trình 2 ẩn:
# 	    a_1*x + b_1*y = c_1
#       a_2*x + b_2*y = c_2
# Các hệ số a1, a2, b1, b2, c1, c2 nhập từ bàn phím. Xét tất cả các trường hợp cụ thể
# Công thức Cramer2 dùng tính hệ phương trình 2 ẩna1 = float(input("Nhập hệ số a1: "))
a2 = float(input("Nhập hệ số a2: "))
b1 = float(input("Nhập hệ số b1: "))
b2 = float(input("Nhập hệ số b2: "))
c1 = float(input("Nhập hệ số c1: "))
c2 = float(input("Nhập hệ số c2: "))
A = a1*b2 - a2*b1
if A != 0:
         A1 = b2*c1 - b1*c2
         A2 = a1*c2 - a2*c1
         x = A1/A
         y = A2/A
         print(f'Nghiệm của hệ phương trình là :{x}')
         print(f'Nghiệm của hệ phương trình là :{y}')
else:
    print("Phương pháp Cramer không hỗ trợ tính khi định thức bằng 0")