# een aantal voorbeelden van het gebruik van modulariteit en scope in Python

a = 2 #globale variabele
l = [1,2]

def f():
    b = 3 #lokale variabele
    return a*b #toegang tot de globale variabele mag

def g(x):
    a = x #lokale variabele op basis van de parameter, dus niet de globale variabele
    b = 3 #gewone lokale variabele
    return a*b

def h(x):
    x[1] = 3

#aanroepen van een functie met daarin een toekenning aan een variabele of een parameter verandert een global niet
print(a)
g(5)
print(a)

#aanroepen van een functie met een toekenning op een mutable variabele (list) verandert de global wel
print(l)
h(l)
print(l)