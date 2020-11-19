# Program to find top 10 common words in a file using touples

userInput = input('Enter a file name: ')

try :
    fileHandle = open(userInput, 'r')
except :
    print(fileHandle, 'is an incorrect file name')
    quit()

histogram = dict()

for words in fileHandle :
    #words = words.rstrip()
    pieces = words.split()
    
    for word in words :
        histogram[word] = histogram.get(word, 0) + 1

lst = list()
for key, val in histogram.items() : 
    newtoup = (val, key)
    lst.append(newtoup)

lst = sorted(lst, reverse=True)


for val, key in lst[:10] :
    print(key, val)