'''
8.4 Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list 
and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
'''

fileName = input('Enter a file name: ')

try : 
    fileHandle = open(fileName, 'r')
except :
    print(fileName, 'Cannot be opened')
    quit()

wordlist = list()

for words in fileHandle :
    words = words.rstrip()
    pieces = words.split()
    
    for letters in pieces : 
        if letters in wordlist :
            continue
        else :
            wordlist.append(letters)
            wordlist.sort()

print(wordlist)

