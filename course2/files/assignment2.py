'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values
and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
'''

fileName = input('Enter a file name: ')

try : 
    fileHandle = open(fileName, 'r')
except :
    print(fileName, 'Cannot be opened')
    quit()

count = 0
total = 0
average = 0

for lines in fileHandle :
    if lines.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        #lines = lines.rstrip()
        startPosition = lines.find(' ')
        value = float(lines[startPosition : ])
        #output = float(value)
        total = value + total
      
average = total/count    

print('Average spam confidence:', average)