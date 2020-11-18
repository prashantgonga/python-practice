# Read contents of a text file, make a histogram and print the word which appeared the most along with the count

fileName = input('Enter the file name: ')
try :
    fileHandle = open(fileName, 'r')
except :
    print(fileHandle, 'is the wrong filenames')

histogram = dict()

for words in fileHandle :
    words = words.split()
    
    for word in words :
        histogram[word] = histogram.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in histogram.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        bigword = word
print(bigcount, bigword)
