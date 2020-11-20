# Fine tuning search using regex

import re

rawdata = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

data = re.findall('^From (\S+@\S+)', rawdata)
print(data)