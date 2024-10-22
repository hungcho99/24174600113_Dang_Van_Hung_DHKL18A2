#đề bài yêu cầu nhập x để tính f(x) = log4(x) + logx(2)

import math 
x = float(input('Nhập giá trị của x: '))
if x > 0 and x != 1:
    F = math.log(x , 4) + math.log(2, x)
    print(f'Giá trị của biểu thức là {F:.2f}.')
else:
    print('X phải lớn hơn 0 và khác 1.')    