# ==, >=, <=, >, <, !=
# Syntax of if
# Indentation
"""if condition:
  statement1
  statement2
  ...
  statementN
statementM
"""
"""
# if
age = float(input("What is your age? Ans: "))

if age >= 18:
  print("Congratulations! You are able to cast your votes!!!")
print("Rest of the program")
"""
"""
# if-else

age = float(input("What is your age? Ans: "))

if age >= 18:
  print("Congratulations! You are able to cast your votes!!!")
else:
  print("You are a Minor!!!")

print("Rest of the program")
"""
"""
# Example:
# Print if a number (int) is odd or even
# even - when a number is divisible by 2 - remainder is 0
# odd - when a number is not-divisible by 2 - remainder is not 0

# %
num = int(input("Enter an integer: "))

if num % 2 == 0:
  print("The number is even.")
else:
  print("The number is odd.")
"""
"""
# elif
'''
if marks >= 60, student is Pass else student is Fail
and the student is pass, then we print the grade
>= 90, grade A
80 to 89, grade B
70 to 79, grade C
60 to 69, grade D
< 60, grade Fail
'''

marks = float(input("Enter your marks: "))

if marks >= 90:
  print("Your grade is 'A'")
elif marks >=80 and marks < 90:
  print("Your grade is 'B'")
elif marks >=70 and marks < 80:
  print("Your grade is 'C'")
elif marks >=60 and marks < 70:
  print("Your grade is 'D'")
else:
  print("Your grade is 'F'")
"""
"""
# Nested elif
marks = float(input("Enter your marks: "))

if marks >= 60:
  print("Congratulations, you have passed in the exam.")
  if marks >= 90:
    print("Your grade is 'A'")
  elif 80 <=marks < 90:
    print("Your grade is 'B'")
  elif 70 <=marks < 80:
    print("Your grade is 'C'")
  else:
    print("Your grade is 'D'")
else :
  print("You have failed, study hard next time")
"""
