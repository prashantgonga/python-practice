# Using regular expression for matching and extracting data

import re

x = 'My 2 favourite numbers are 8 and 28'
y = re.findall('[0-9]+', x)
print(y)