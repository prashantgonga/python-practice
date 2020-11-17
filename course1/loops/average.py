# Simple progam to count and calculate sum and average using for loop

counter = 0
sum = 0
print('Before:', counter)

for number in [9, 41, 12, 3, 74, 15] : 
    counter = counter + 1
    sum = sum + number
    print(counter, sum, number)

print('After', counter, sum, sum/counter)
