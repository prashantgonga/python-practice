# Take a filename as user input and count the number of subject lines in the given file 

userInput = input('Enter the file name: ')
fileHandle = open(userInput, 'r')
count = 0

for line in fileHandle :
    if line.startswith('Subject') :
        count = count + 1

print('There were', count, 'subject lines in', userInput)