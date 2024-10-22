giay_su_dung = float(input("Nhập số giây sử dụng bóng đèn: "))
if giay_su_dung > 0:
   #đổi giây ra giờ
   h = giay_su_dung/3600
   print(f"Số giờ điện đã dùng là {h}")
   sodien = (220 * 2.7 * h)/1000
   print(f"Số điện đã sử dụng là {sodien}")
   bill = (sodien * 7000)
   print(f"Số tiền điện phải trả là {bill}vnd.")
else:
   print("Số giây sử dụng không hợp lệ.")