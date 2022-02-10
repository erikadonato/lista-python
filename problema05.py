soma = media = maior = menor = contador = 0
produto = 1
while True:
    numero = float(input('Digite um número positivo: '))
    while numero < 0:
        print('Digite um número positivo!')
        numero = float(input('Digite um número positivo: '))
    if numero !=0:
        soma += numero
        contador += 1
        produto *= numero
        media = soma/contador
        if contador == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    else:
        print('A soma dos números é', soma)
        print('A média dos números é', round(media, 1))
        print('O produto dos números é', round(produto, 1))
        print('O menor número digitado foi', menor)
        print('O maior número digitado foi', maior)
        break