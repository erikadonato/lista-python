n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
for x in range (n1, n2+1): 
    x-1
    fatorial = 1
    for y in range (1, x+1): 
        if y == 0:
            break
        fatorial *= y
        y-1
    print('Fatorial de', x, '=', fatorial)