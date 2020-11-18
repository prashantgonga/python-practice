# Make a histogram from user input

fileName = input('Enter a file name: ')

try :
    fileHandle = open(fileName, 'r')
except:
    print(fileName, 'is not a correct file name')
    quit()

histogram = dict()
for words in fileHandle :
    words = words.rstrip()
    pieces = words.split()

    for piece in pieces :      
        histogram[piece] = histogram.get(piece, 0) + 1

print(histogram)
