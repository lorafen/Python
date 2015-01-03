# Modulo operation without using %

def modulo(dividend, divisior):
    reminder = dividend - divisior * int(dividend/divisior)
    return reminder

dividend = int(input('Podaj liczbe: '))
divisior = int(input('Podaj dzielnik:  '))

print(modulo(dividend, divisior))
