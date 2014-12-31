# Counting median
import math

def mediana(tablica, sizeOfTable):
    tablica = wypelnijTablice(tablica, sizeOfTable)
    tablica = sortowanie(tablica)
    if (sizeOfTable%2 == 0):
        result = (tablica[sizeOfTable//2 - 1] + tablica[sizeOfTable//2])/2
    else:
        result = tablica[sizeOfTable // 2] 
    return result

def sortowanie(tablica):
    tablica.sort() 
    print(tablica)
    return tablica

def wypelnijTablice(tablica, sizeOfTable):
    for x in range(sizeOfTable):
        tablica.append( int( input() ) )
    return tablica

tablica = []
sizeOfTable = int( input('Rozmiar tablicy: ') )
print(sizeOfTable)
print( mediana(tablica, sizeOfTable) )