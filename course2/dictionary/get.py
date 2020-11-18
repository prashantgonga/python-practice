# Add a list of names and count them using dictionary and get method

counts = dict()
names = ['Jack', 'Jill', 'John', 'Jack', 'Jill', 'Jill']

for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)