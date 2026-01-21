"""name = "John"
age = 20
language = "Python"
hours = 3
# John is 20 years old. He studies Python 3 hours a day.
print(name,"is",age, "years old.", "He studied", language,hours,"hours a day.")

# Using f-string
print(f"{name} is {age} years old. He studied {language} {hours} hours a day.")
"""
name = "John"

subject_1 = 80
subject_2 = 49
subject_3 = 67

# print(f"{name} scored {subject_1 + subject_2 + subject_3} marks in total.")
percent = (subject_1 + subject_2 + subject_3) / 3
print(f"{name} scored {percent:.2f} % in total.")