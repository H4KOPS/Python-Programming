"""
When all the length of the sides is know in a, b and c.

Fining the semi-perimiter (s) = (a + b + c) / 2
Area = Square root of (s * (s-a) * (s-b) * (s-c))
"""

a = float(input("Enter a side length: "))
b = float(input("Enter b side length: "))
c = float(input("Enter c side length: "))
s = (a + b + c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print("The area of the triangle is ", round(area, 2))