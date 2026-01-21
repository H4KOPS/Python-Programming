# Tuple
# (item1, item2, ......)
# sequence of items as a collection
"""
t1 = ("Python", 10, 1.5, True, [1,2,3], (10,20))
print(type(t1))
print(len(t1))

# Accessing items of a tuples -index
print(t1[-1][2])
"""
'''
t1 = (10, "list")
print(type(t1)) # type = Tuple
print(t1)
'''
"""
# Typecasting
# Converting from integer to tuple
l1 = [1,2,3]
print(l1, type(l1))
t1 = tuple(l1)
print(t1, type(t1))
"""

# Converting tuple to list
fruits = ("Mango", "Papaya", "Banana")
print(fruits, type(fruits))
converted_into_list = list(fruits)
print(converted_into_list, type(converted_into_list))