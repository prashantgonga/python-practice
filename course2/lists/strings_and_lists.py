# Using strings and lists

greeting = "Hello Good Morning"

pieces = greeting.split()
print(pieces)
print(len(pieces))
print(pieces[1])

for words in pieces :
    print(words)

for letters in pieces[1] :
    print(letters)