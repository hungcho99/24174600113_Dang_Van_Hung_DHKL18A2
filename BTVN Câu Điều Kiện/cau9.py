# 9. Tính cước tacxi: 
# Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:

print("1. Xe 4 chỗ\n2. Xe 7 chỗ")
loaixe = float(input("Nhập loại xe bạn muốn tính: "))
time_doi = float(input("Nhập thời gian đợi theo phút(dưới 5 phút sẽ được free cước): "))


# Tiền chờ: 05 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800đ/phút.
cuoc_doi = 0
if time_doi  < 5:
    print("Bạn đã được miễn phí cước đợi.")
else:
    cuoc_doi = (time_doi - 5) * 800
    print(f"Số tiền cước đợi phải trả là {int(cuoc_doi)}vnđ sẽ được cộng vào số tiền bạn phải trả.")


if loaixe != 1 and loaixe != 2:
        print("Bạn chỉ được chọn 1 trong 2 loại xe.")

# -	Loại xe 4 chỗ
#   Giá mở cửa			11.000 đồng/0.8km
#   Trong phạm vi 20km 	12.100đ/km
#   Từ km thứ 21 trở đi 		10.000 đồng/km
elif loaixe == 1:
    print("Bạn đã chọn loại xe 4 chỗ.")
    km = float(input("Nhập số km bạn muốn di chuyển: "))
    if km < 0:
        print("Số km không được nhỏ hơn 0.")
    elif km <= 20:
        #đi dưới 20km thì trừ đi 0.8km giá mở cửa
        gia_mua_cua = 11000
        km_dichuyen = ((km - 0.8)) * 12100
        print(f"Số tiền phải trả là {int(gia_mua_cua + km_dichuyen + cuoc_doi)}vnđ.")

    elif km > 20:
        #đi hơn 20km thì trừ đi 0.8 với 20km đầu.
        gia_mua_cua = 11000
        km_20 = 20 * 12100
        km_dichuyen = (km - (0.8 + 20)) * 10000
        print(f"Số tiền phải trả là {int(gia_mua_cua + km_20 + km_dichuyen + cuoc_doi)}vnđ.")



# -	Loại  xe 7 chỗ
#   Giá mở cửa			13.000 đồng/0.8km
#   Trong phạm vi 30km 	14.100đ/km
#   Từ km thứ 31 trở đi 		12.000 đồng/km

elif loaixe == 2:
    print("Bạn đã chọn loại xe 7 chỗ.")
    km = float(input("Nhập số km bạn muốn di chuyển:"))
    if km < 0:
        print("Số km không được nhỏ hơn 0.")
    elif km <= 30:
        #đi dưới 30km thì trừ đi 0.8km giá mở cửa
        gia_mua_cua = 13000
        km_dichuyen = ((km - 0.8)) * 14100
        print(f"Số tiền phải trả là {int(gia_mua_cua + km_dichuyen + cuoc_doi)}vnđ")

    elif km > 30:
        #đi hơn 30km thì trừ đi 0.8 với 30km đầu.
        gia_mua_cua = 13000
        km_20 = 20 * 12100
        km_dichuyen = (km - 0.8 - 30) * 12000
        print(f"Số tiền phải trả là {int(gia_mua_cua + km_dichuyen + km_20 + cuoc_doi)}vnđ")

      
