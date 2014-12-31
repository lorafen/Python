# Full the table random number :D

import random

def wypelnijTabliceA(tablica, n):
    for x in range(n):
        # even - random number 0-10 
        if (x%2 == 0):
            tablica.append( random.randint(0,10) )
        else:
            tablica.append(99)
    print(tablica)
    return
def wypelnijTabliceB(tablica, n):
    for x in range(n):
        # even - random number {1, 5, 19, 31}
        if (x%2 == 0):
            tablica.append( random.choice([1, 5, 19, 31]) )
        # odd - 0
        else:
            tablica.append(0);
    print(tablica)
    return


tablica = []
# size of table
sizeOfTable = int(input('Size of table: '))

wypelnijTabliceA(tablica, sizeOfTable)
tablica.clear()
wypelnijTabliceB(tablica, sizeOfTable)