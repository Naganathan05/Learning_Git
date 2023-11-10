a = int(input("Enter The Length Of a:"))
b = int(input("Enter The Length Of b:"))
c = int(input("Enter The Length Of c:"))
d = True

s = (a + b + c)/2

area = ((s*(s - a)*(s - b)*(s - c)) ** 0.5)
print(area)

if a % 2 == 0:
    print(a," Is a even number.")
else:
    print(a," Is a odd number.")

print(type(d))

#My Comment 
