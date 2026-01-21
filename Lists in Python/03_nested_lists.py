# Lists inside a list
"""
l1 = [5, 1.5, "Python", True, None, [1, 2, 3], [7, 8]]
print(len(l1))
print(l1[-1][])
"""

l2 = [[1,2], [3,4], [5,6,[0,1]]] 
print(len(l2))
print(l2[-1][2][1])