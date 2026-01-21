"""
student1 = {'Maths': 80.5, 'English': 90, 'Science': 89.5}
print(student1)
# fetch the marks for 'Science'
print(student1['Science'])
# get()
print(student1.get('Science'))
"""
"""
employee1 = {'id': 1001, 'Name': 'John', 'Salary': 10000}
# print(employee1.get('id', 8217464708))
# Membership operator (in, not in)
# print('Name' in employee1)

# Key value pairs
sem1_marks = {'Maths': 78.5, 'English': 71.0, 'Physics': 86.5}
sem2_marks = {'Chemistry': 81.5, 'Biology': 90.5}
# update()
sem1_marks.update(sem2_marks)
print(sem1_marks)
"""
"""
groceries_1 = {'Milk': 50, 'Rice': 75, 'Dal': 20}
groceries_2 = {'Rice': 110, 'Bread': 30}

groceries_1.update(groceries_2)
print(groceries_1)

# pop() - Delete
groceries_1.pop('Milk')
print(groceries_1)
"""
"""
# Keys cannot be duplicated in the dictionary
groceries_1 = {'Milk': 50, 'Rice': 75, 'Milk': 20}
print(groceries_1)
"""
# not allowed keys - list, set, dict => mutable datdtypes
# allowed keys - str, int, float, bool, tuple => immutable datatypes
# keys of a dictionary can only be mutable datatypes!!

# Values can be any datatypes
student1 = {'id': 1001, 'name': 'John', 'marks': {'eng':89.5,'chem':71.2,'maths':81.0}}
print(student1['marks']['eng'])
# Can we fetch keys? Yes
# keys()
print(student1.keys())
# values()
print(student1.values())
# items()
print(student1.items())
print(type(student1.items()))
