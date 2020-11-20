# Read data from a file and find information using regex

import re

userInput = input('Enter a file name: ')

try :
    userData = open(userInput, 'r')
except :
    print(userInput, 'is not the correct file name')
    quit()

numlist = list()
for lines in userData :
    output = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', lines)
    if len(output) != 1 :
        continue
    num = float(output[0])
    numlist.append(num)

print('Maximum:', max(numlist))
