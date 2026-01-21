# Sets are non-sequential collection of items (No indexing in sets is allowed)
# Comma seperated elements enclosed within {}
"""
set1 = {10, "Python", 2.5}
print(set1)
print(type(set1))

# Length of the set
print(len(set1))
"""
"""
# sets do not allow duplicate elements
l1 = [10,2.5,10,30,10]
print(l1, type(l1))
s1 = {10,2.5,10,30,10}
print(s1, type(s1))
"""
"""
# Basic Operations in sets
nums = {1,2,3,4,5,-1}

# Membership operators (in, not in)
print(1 in nums)
print(10 in nums)
print(-1 not in nums)
print(10 not in nums)

# Concatination with sets
nums_1 = {1,3,5,0,-1}
nums_2 = {3,5}
print(nums_1  nums_2)
"""
"""
# Typecasting (Converting into sets from tuple)
# sets are non sequencetial or onordered data.
weekdays = ("Mon","Tue","Wed","Thur","Fri","Sat","Sun")
print(weekdays, type(weekdays))
converted_week = set(weekdays)
print(converted_week)
"""

# Are sets mutable or immutable?
set1 = {2,0,-1}
print(set1)
# add()
set1.add(5)
print(set1)
# set1.add(5) # Multiple elements are not allowed in sets
# print(set1)
# remove()
set1.remove(0)
print(set1)
# discard()
set1.discard(0)
print(set1)
