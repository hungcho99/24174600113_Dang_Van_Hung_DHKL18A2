import math
x = float(input("Nhập x:"))
fx = ( (-x) + math.sqrt((x**2) + 4)) / (((x ** 4) + 1)) ** (1/7)
print(f'Kết quả là {fx:.2f}')