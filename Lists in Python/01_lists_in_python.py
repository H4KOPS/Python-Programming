# name = "John"
# age = 20
# percent = 85.5
"""
student = ["John", 20, 85.5]
print(type(student))    # type= "lists" - Any type of 
print(student)
"""
"""
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week)
print(f"Last day of the week is {days_of_week[6]}") # Positive Index

# Length of the list => The number of items/elements in the list.
print(len(days_of_week))
print(f"Last day of the week is {days_of_week[-1]}") # Negative Index

print(days_of_week[8])
"""
"""
# Slicing of lists.
my_lists = [5, 9, 5, 4, 0, 9, 12]
print(my_lists[2:5:1])
"""
"""
# Concatination of Lists:
l1 = [1, 7, 2]
l2 = [3, 5]
print(l1 + l2)
"""
"""
# Repetation of Lists: 
l1 = [1, 7, 2]
l2 = [3, 5]
print(l2 * 3)
"""
# append()
# adds an item to the end of the list.

fruits = ['Mango', 'Apple', 'Orange'] 

"""
# Syntax: list.append(item)
fruits.append('Banana') # List gets updated of above. Its called mutability.
print(fruits)
"""
"""
# insert
# adds an element before the specified index
# syntax: list.insert(index, item)
fruits.insert(2, "Banana")
print(fruits)
"""
"""
# extend()
# remove()
# pop()

# fruits.extend(['Banana', 'Grapes'])
# print(fruits)

# fruits.remove('Mango')
# print(fruits)

# fruits.pop(2) # In bracket we can ether use elements or keep it blank.
# print(fruits)
"""
"""
# reverse()
# sort()
# count()
# membership operation

# reverse()
# days_of_week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# days_of_week.reverse()
# print(days_of_week)

# sort()
# nums = [4, 9, 3, 7, 8, 1, 5]
# nums.sort(reverse=True) # For accending normal () for decending order inside the bracket(reverse=True)
# print(nums)

# count()
# nums = [0, 1, 3, 4, 5, 8, 9,4,2,1,5,2,]
# print(nums.count(5))

# membership operator (in , not in)
language = ["Python", "Java", "C++", "Python"]
print("Java" in language)
print("MongoDB" in language)
print("Python" not in language)
print("Typescript" not in language)
"""

