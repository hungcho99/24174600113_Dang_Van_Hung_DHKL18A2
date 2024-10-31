
# 8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
# Nếu điểm A thì phân loại là sinh viên xuất sắc, 
# điểm B là sinh viên loại giỏi, 
# điểm C là sinh viên loại khá, 
# điểm D là sinh viên loại trung bình, 
# điểm E là sinh viên loại yếu, 
# điểm F là sinh viên xếp loại kém.

#dùng upper() để sửa chữ thường thành chữ hoa(chương 6 lms)

# Nhập điểm và chuyển thành chữ hoa
input_ = input("Nhập điểm: ").upper()

# Phân loại sinh viên
if input_ == "A":
    print("Sinh viên loại xuất sắc.")
elif input_ == "B":
    print("Sinh viên loại giỏi.")
elif input_ == "C":
    print("Sinh viên loại khá.")
elif input_ == "D":
    print("Sinh viên loại trung bình.")
elif input_ == "E":
    print("Sinh viên loại yếu.")
elif input_ == "F":
    print("Sinh viên xếp loại kém.")
else:
    print("Điểm không hợp lệ.")
