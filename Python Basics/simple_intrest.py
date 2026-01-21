"""
Simple Intrest = (P * R * T) / 100
P = Principal amount
R = Rate of interest
T = Time duration
"""
principal = float(input("Enter your principal: "))
rate = float(input("Enter your rate: "))
time = float(input("Enter your time: "))
si = (principal * rate * time) / 100
print("Simple Intrest: ", si)
