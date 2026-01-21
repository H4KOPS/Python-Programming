"""
Compound Intrest =
Amount = P(1 + r/100)  ** T
ci = Amount - P

"""

principal = float(input("Enter your principal: "))
rate = float(input("Enter your rate: "))
time = float(input("Enter your time: "))
amount = principal * pow((1 + rate/100), time)
print(round(amount, 2))
ci = amount - principal
print("Compound Intrest", round(ci, 2))