# Frozen sets are immutable sets
fs1 = frozenset({10,20,30})
print(fs1, type(fs1))
fs2 = frozenset({10,100,200,50})
print(fs2, type(fs2))

print(fs1 | fs2)
#  & = intersection
# | = union
# - = Difference Between
