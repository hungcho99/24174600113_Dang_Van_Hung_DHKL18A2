# 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền
# lương thực sự mà nhân viên đó nhận được).
# Với các thông số giả sử như sau
# • 30% thuế thu nhập nếu lương là 15 triệu.
# • 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# • 10% thuế thu nhập nếu lương dưới 7 triệu.

luong_goc = float(input("Nhập số lương gốc nhận được: "))
if (luong_goc < 7000000):
    thue = 10/100 * luong_goc
if (7000000 <= luong_goc) and (luong_goc < 15000000):
    thue = 20/100 * luong_goc
if (luong_goc > 15000000):
    thue = 30/100 * luong_goc
print(f"Thuế thu nhập {int(thue)}vnđ", f"\nLương ròng {int(luong_goc - thue)}vnđ")





