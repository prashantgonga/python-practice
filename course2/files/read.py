# Reading contents of a text file

fileHandle = open('mbox.txt', 'r')

for lines in fileHandle :
    print(lines)