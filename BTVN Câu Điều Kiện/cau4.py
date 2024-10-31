# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

#Nếu là tam giác thường 
# a + b > c và a + c > b và c + b > a
dk1 = (a + b) > c
dk2 = (a + c) > b
dk3 = (c + b) > a

if dk1 == False or dk2 == False or dk3 == False:
    print(f"Ba cạnh {a, b, c} không phải ba cạnh của tam giác.")

#Nếu là tam giác vuông thì a^2 + b^2 = c^2
vuong = ((a**2) + (b**2)) == (c**2)
#Nếu là cân thì a = b hoặc b = c hoặc c = a
can = (a == b) or (b == c) or (c == a)
#Nếu là vuông cân thì phải vuong, can phải là true
if vuong == True and can == True:
    vuong_can = True
else:
    vuong_can = False
#Nếu là tam giác đều thì a = b = c
deu = (a == b == c)

if deu == False:
   if vuong_can == True:
     print(f"Ba cạnh {a, b, c} tạo thành tam giác vuông cân.")
   elif vuong_can == False:
     if vuong == True: 
         print(f"Ba cạnh {a, b, c} tạo thành tam giác vuông.")
     elif can == True:
        print(f"Ba cạnh {a, b, c} tạo thành tam giác cân.")
    
elif deu == True:
   print(f"Ba cạnh {a, b, c} tạo thành tam giác đều.")

else:
   print(f"Ba cạnh {a, b, c} tạo thành tam giác thường.")
   