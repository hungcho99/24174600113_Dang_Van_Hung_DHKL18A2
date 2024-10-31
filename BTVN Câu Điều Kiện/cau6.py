#Viết chương trình thể hiện menu lựa chọn gồm các thể loại phim hiện đang có trong rạp chiếu phim ABC. 
# Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem (Phim tình cảm, Phim kinh dị, Phim hoạt hình, Phim khoa học viễn tưởng)

print("Đây là rạp chiếu phim ABC.")
print("Vui lòng chọn loại phim muốn xem:\n1. Phim tình cảm\n2. Phim kinh dị\n3. Phim hoạt hình\n4. Phim khoa học viễn tưởng")

loaiphim = int(input("Nhập thứ tự của loại phim muốn xem: "))

if loaiphim >= 1 and loaiphim <=4:
   if loaiphim == 4:
      print("Bạn đã lựa chọn phim khoa học viễn tưởng.")
   elif loaiphim == 3:
      print("Bạn đã lựa chọn phim hoạt hình.")
   elif loaiphim == 2:
      print("Bạn đã lựa chọn phim kinh dị.")
   elif loaiphim == 1:
      print("Bạn đã lựa chọn phim tình cảm.")  

else:
   print("Chỉ nhập theo thứ tự 1 đến 4.")

