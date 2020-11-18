# Count the number of lines in a file

fileHandle = open('mbox.txt', 'r')
counter = 0

for lines in fileHandle :
    counter = counter + 1
print(counter)