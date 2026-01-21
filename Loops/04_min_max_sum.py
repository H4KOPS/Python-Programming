"""
scores = [2,45,102,34,63,2,46,78,35,28,34]
total = 0
for score in scores:
    total = total + score

print(f"Total runs scored by India is {total}")
"""
scores = [2,45,102,34,63,2,46,54,35,28,34]
# total = sum(scores)
# print(f"Total runs scored by India is {total}")

# Highest Score

highest = scores[0] # assume that the first value is highest

for score in scores:
    if highest < score:
        highest = score

print(f"Most Valueable score is {highest}")
