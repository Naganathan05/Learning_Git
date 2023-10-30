a = int(input("Enter The Length Of a:"))
b = int(input("Enter The Length Of b:"))
c = int(input("Enter The Length Of c:"))

s = (a + b + c)/2

area = ((s*(s - a)*(s - b)*(s - c)) ** 0.5)
print(area)