# Add a list of names and count them using dictionary

counts = dict()
names = ['Jack', 'Jill', 'John', 'Jack', 'Jill', 'Jill']

for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts) 