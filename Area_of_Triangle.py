#if we know all sides of the triangle
a=float(input("Enter the side1:"))
b=float(input("enter the side2:"))
c=float(input("enter the side3:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) **0.5
print(round(area,2))
