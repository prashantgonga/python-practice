# count the number of words in a webpage

import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()

for words in fhandle :
    words = words.decode().split()
    for words in words :
        count[words] = count.get(words, 0) + 1

print(count)
