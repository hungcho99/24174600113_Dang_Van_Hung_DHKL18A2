# 2. Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím?

x = float(input("Nhap X:"))
y = float(input("Nhap Y:"))
a = float(input("Nhap A:"))
b = float(input("Nhap B:"))
r = float(input("Nhap R:"))

do_dai_IM = (((x - a)** 2 ) + ((y - b)** 2)) ** 1/2

#so sanh im voi r
if do_dai_IM <= r:
    print(True)
else:
    print(False)
