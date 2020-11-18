# Re-writing the following program for better error handling
# Take a filename as user input and count the number of subject lines in the given file 

fileName = input('Enter a file name: ')

try : 
    fileHandle = open(fileName, 'r')
except :
    print(fileName, 'Cannot be opened')
    quit()

count = 0

for lines in fileHandle :
    if lines.startswith('Subject:') :
        count = count + 1

print('There were', count, 'subject lines in', fileName)
