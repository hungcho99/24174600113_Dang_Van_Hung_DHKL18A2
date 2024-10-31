# 3. Viết chương trình tìm số lớn nhất trong 3 số bằng Python
a, b, c = map(float, input("Nhập 3 số: ").split())
if a > b and a > c:
    print(f"{a} là số lớn nhất.")
elif b > a and b > c:
    print(f"{b} là số lớn nhất.")
else:
    print(f"{c} là số lớn nhất.")
