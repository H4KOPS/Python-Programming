countries = ["India", "United States", "Australia", "Ireland", "Sri Lanka", "Iceland", "Cuba", "Iran","Poland"]

# count all the countries which are starting with "I"
# also, print all these countries as a list
counter = 0
output = []
for country in countries:
    if country.startswith("I"):
        counter = counter + 1
        output.append(country)

print(counter)
print(output)
