'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum 
loop to find the most prolific committer.
'''

userInput = input('Enter the file name: ')

try :
    fileHandle = open(userInput, 'r')
except :
    print(userInput, 'is not the correct filename')

histogram = dict()

for words in fileHandle :
    words = words.rstrip()
    if not words.startswith('From ') :
        continue
    data = words.split()
    pieces = data[1]
    histogram[pieces] = histogram.get(pieces, 0) + 1
  
finalCount = None
finalEmail = None

for email, count in histogram.items() :
    if finalCount is None or count > finalCount :
        finalCount = count
        finalEmail = email

print(finalEmail, finalCount)




        
