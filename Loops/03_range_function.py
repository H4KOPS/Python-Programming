# range() - built-in function used to generate sequence of integers in a given interval.
# range(start,stop,step) stop is not included
# for i in range(start,stop,step):
    # Statements
"""
for i in range(2,12,2):
    print(i)
"""
"""
# reverse order => 20 to 10 (excluded 10)
for i in range(20,10,-1):
    print(i)
"""
"""
# Countdown from 10 to 1 (1 is included)
for i in range(10,0,-1):
    print(i)
print("Happy New Year 2026..!")
"""

# range(start,stop) ==> step => 1 by default
# range(stop) => 0 to stop -1 with a step of 1, start => 0 by default

# Example
groceries = ['salt', 'milk', 'sugar']
for index in range(len(groceries)):
    print(index)
