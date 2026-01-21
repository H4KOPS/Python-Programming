# while continue:
#     statements
"""
for i in range (1, 5, 1):
    print(i)
"""
"""
num = 1

while num < 5:
    print(num)
    num = num + 1
"""
correct_password = "Python"

while True: # Infinite Loop
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Password is correct! Congrats.!")
        break
    else:
        print("Wrong password, try again.")
print("Logged in!")
