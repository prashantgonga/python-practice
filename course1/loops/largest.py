# Finding the largest number using for loop

largest_so_far = -1 
print('Before:', largest_so_far)

for number in [9, 41, 12, 3, 74, 15] :
    if number > largest_so_far :
        largest_so_far = number
    print(largest_so_far)

print('After:', largest_so_far)
print('All done!')