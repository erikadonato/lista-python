numero = int(input('Digite um número inteiro positivo: '))
while numero <= 0:
    numero = int(input('Digite um número inteiro positivo: '))
for x in range(numero):
    if numero % (x+1) == 0:
        print(x+1, 'é divisor de', numero)
        proximo = x+1
        if proximo != 1:
            for y in range(proximo):
                if proximo == numero:
                    break
                if proximo % (y+1) == 0:
                    print(y+1, '> é divisor de', proximo)