# Check which string is longer
def ktoryDluzszy(string1, string2):
    if ( len(string1) > len(string2) ):
        print('Dluzszym wyrazem jest: ' + string1)
    elif ( len(string1) < len(string2) ):
        print('Dluzszym wyrazem jest: ' + string2)
    else:
        print('Oba wyrazy maja tyle samo znakow.')
    return

# Check how many times char of first string occured in the second string
def howManyTimes(string1, string2):
    x = 0
    tablica = []
    for c1 in string1:
        for c2 in string2:
            if c1 == c2:
                x += 1;
        tablica.append(x)
        x = 0
    showTable(tablica, string1)
    return

# Beautiful print
def showTable(tablica, string1):
    print('Wystapienia poszczegolnych znakow: ')
    for c, v in zip(string1, tablica):
        print(c + ': ' + str(v) )
    return

# Get from user two strings
string1 = input('Get a string 1: ')
string2 = input('Get a string 2: ')

ktoryDluzszy(string1, string2)
howManyTimes(string1, string2)