numero = int(input('Digite um número entre 1000 e 9999:'))
maioresquerda = maiordireita = extremosiguais = 0
while True:
    if numero < 1000 or numero > 9999:
        print('Número inválido!')
        numero = int(input('Digite um número entre 1000 e 9999:'))
    auxiliar = numero
    for x in range(numero, 10000):
            lista = [int(a) for a in str(auxiliar)]
            if lista[0] > lista[3]:
                maioresquerda+=1
            if lista[0] < lista[3]:
                maiordireita+=1
            if lista[0] == lista[3]:
                extremosiguais+=1
            auxiliar+=1
    print(maioresquerda, 'vezes o dígito da esquerda é maior')
    print(maiordireita, 'vezes o dígito da direita é maior')
    print(extremosiguais, 'vezes o dígito da esquerda é igual ao da direita')
    break