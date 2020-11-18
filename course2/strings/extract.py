# Extracting domain name from an email address 

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

startPosition = data.find('@')
endPosition = data.find(' ', startPosition)
domain = data[startPosition+1 : endPosition]
print(domain)