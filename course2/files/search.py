# Search through a file

fileHandle = open('mbox-short.txt', 'r')

for line in fileHandle :
    if line.startswith('From: ') :
        print(line)