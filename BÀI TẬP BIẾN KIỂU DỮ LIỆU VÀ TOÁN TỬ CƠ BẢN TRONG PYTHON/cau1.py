#viết công thức tính  tính diện tích xung quanh, diện tích toàn phần và thể tích khối trụ, input là r và h;

#Diện tích xung quanh (Sxq): S = 2 * pi * r * h;
#Diện tích toàn phần (Stp): = (2 * pi * r) * (h + r);
#Thể tích khối trụ (V): V = pi * (r ** 2) * h;
#float là số thực
#int là số nguyên


input_r = float(input("Nhập bán kính của mặt đáy:"))
input_h = float(input("Nhập chiều cao:"))

if(input_r < 0 or input_h < 0):
    print("Bán kính đáy hoặc chiều cao không được âm.")

else:
    pi = 3.14
    sxq = 2 * pi * input_r * input_h
    stp = ( 2 * pi * input_r) * (input_h + input_r)
    thetich = pi * (input_r ** 2) * input_h
    print(f"Diện tích xung quanh là: {sxq:.2f}")
    print(f"Diện tích toàn phần là: {stp:.2f}")
    print(f"Thể tích là: {thetich:.2f}")





   


