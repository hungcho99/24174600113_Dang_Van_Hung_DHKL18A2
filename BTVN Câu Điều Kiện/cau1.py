# 1. Tính năm nhuận. Năm thứ n là nhuận nếu nó chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 

nam = (int(input("Nhập năm cần tính: ")))
if nam % 4 == 0:
  if nam % 100 !=0 or nam % 400 == 0:
    print(f"Năm {nam} là năm nhuận.")
  else:
    print(f"Năm {nam} không là năm nhuận.")

else:
  print(f"Năm {nam} không là năm nhuận.")


