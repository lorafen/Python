# Standard deviation
import math

def odchylenieStandardowe(tablica):
    result = 0.0
    srednia = sredniaArytmetyczna(tablica)
    for i in tablica:
        result += math.pow((float(i) - srednia), 2)
    return math.sqrt(result)

def sredniaArytmetyczna(tablica):
    sum = 0
    for i in tablica:
        sum += i
    result = sum / len(tablica) 
    return result

# size of table
sizeOfTable = int(input('Podaj rozmiar tablicy: '))
# create a table
table = []
for i in range(sizeOfTable):
    table.append(int(input('Podaj liczbe: ')))

result = odchylenieStandardowe(table)
print(result)