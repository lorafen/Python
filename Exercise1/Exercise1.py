# Exercise - Count the power for INT:D
def potega(liczba, doPotegi):
    result = 1;
    
    if (doPotegi < 0):
        for x in range(abs(doPotegi)):
            result *= 1.0/liczba
        print('potega < 0')
    elif (doPotegi == 0):
        result = result
        print('potega = 0')
    else:
        for x in range(doPotegi):
            result *= liczba
        print('potega > 0')
    return result

# ask about number and the power
print('The power of the number!')
liczba = input('Number: ')
doPotegi = input('Power: ')

print( potega(int(liczba), int(doPotegi)) )



