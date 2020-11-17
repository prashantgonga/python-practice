# Using functions and return to greet in different languages

def greet (lang) :
    if lang == 'fr' :
        return 'Bonjour'
    elif lang == 'es' :
        return 'Hola'
    else :
        return 'Hello'

print (greet('fr'), 'Neo')
print (greet('es'), 'John Wick')
print (greet('potato'), 'Karen')