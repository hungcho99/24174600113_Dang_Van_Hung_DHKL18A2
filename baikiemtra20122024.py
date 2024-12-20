#đề 2

dsmathang = []
#bài sử dụng try except để bắt lỗi khi nhập sai kiểu dữ liệu

#Lựa chọn 1: xem danh sách mặt hàng
luachon = input("Nhập lựa chọn: ")
if luachon == "1":
    if dsmathang == []:
        print("Danh sách mặt hàng rỗng")
    else:
        for i in dsmathang:

            print(i)

#Lựa chọn 2: nhập thông tin mặt hàng từ bàn phím
if luachon == "2":
    try:
       mahang = int(input("Nhập mã hàng: "))
       tenhang = str(input("Nhập tên hàng: "))
       donvitinh = int(input("Nhập đơn vị tính: "))
       dongia = int(input("Nhập đơn giá: "))
       soluong = int(input("Nhập số lượng: "))
       dsmathang.append({
              "mahang": mahang,
              "tenhang": tenhang,
              "donvitinh": donvitinh,
              "dongia": dongia,
              "soluong": soluong
         })
    except ValueError:
        print("Nhập sai kiểu dữ liệu")
    
