'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
for each of the messages. You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

'''

userInput = input('Enter the file name: ')

try :
    fileHandle = open(userInput, 'r')
except :
    print(fileHandle, 'is an incorrect filename')
    quit()

histogram = dict()

for words in fileHandle :
    words = words.rstrip()
    if not words.startswith('From ') :
        continue
    words = words.split()
    words = words[5]
    words = words[:2]
    histogram[words] = histogram.get(words, 0) + 1

lst = list()
for value, key in histogram.items() :
    lst.append((value, key))

lst.sort()

for value, key in lst :
    print(value, key)

    
    
    
    

     

