# Find a domain name from an email address using split

rawdata = 'FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008'
words = rawdata.split()
email = words[1]

pieces = email.split('@')
domain = pieces[1]
print(domain)