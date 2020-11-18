# Search through a file

fileHandle = open('mbox-short.txt', 'r')

for line in fileHandle :
    line = line.rstrip()
    if line.startswith('From: ') :
        print(line)