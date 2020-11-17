# Find the smallest number using for loop

smallest = None
print('Smallest', smallest)

for number in [9, 41, 12, 3, 74, 15] :
    if smallest is None : 
        smallest = number
    elif number < smallest:
        smallest = number
    print(smallest, number)

print('After', smallest)
print('All Done!')