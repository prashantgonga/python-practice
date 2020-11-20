# Read rawdata.txt file find all the numbers in that file and add them

import re

userInput = input('Enter a file name: ')

try :
    fileHandle = open(userInput, 'r')
except :
    print(fileHandle, 'is not the correct file name')
    quit()

sumtotal = 0

for lines in fileHandle :
    numbers = re.findall('([0-9]+)', lines)
  
    for output in numbers :
        sumtotal = sumtotal + int(output) 

print(sumtotal)