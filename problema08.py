lista_par = []
lista_impar = []
while True:
    numero = int(input('Digite um número inteiro:'))
    if numero !=0:
        if numero % 2 == 0:
            lista_par.append(numero)
        else:
            lista_impar.append(numero)
    else:
        break
if len(lista_par) == 0:
    print('Lista de pares vazia')
    print('Menor ímpar:', min(lista_impar))
    print('Maior ímpar:', max(lista_impar))
    print('Média ímpar:', sum(lista_impar)/len(lista_impar))
if len(lista_impar) == 0:
    print('Menor par:', min(lista_par))
    print('Maior par:', max(lista_par))
    print('Média pares: ', sum(lista_par)/len(lista_par))
    print('Lista de ímpares vazia')
elif len(lista_par) and len(lista_impar != 0):
    print('Menor par:', min(lista_par))
    print('Maior par:', max(lista_par))
    print('Média pares: ', sum(lista_par)/len(lista_par))
    print('Menor ímpar:', min(lista_impar))
    print('Maior ímpar:', max(lista_impar))
    print('Média ímpar:', sum(lista_impar)/len(lista_impar))
