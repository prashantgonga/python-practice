# Search using boolean variable in for loop

found = False
print('Before', found)

for number in [9, 41, 12, 3, 74, 15] :
    if number == 3 :
        found = True
        break 
    print(found, number)
    

print('After', found)
print('All Done!')