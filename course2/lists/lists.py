# Calculating average value from user input using list

numList = []

while True :
    userInput = input('Enter a number: ')
    if userInput == 'done' :
        break
    value = float(userInput)
    numList.append(value)

average = sum(numList) / len(numList)
print(average)