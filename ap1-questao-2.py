ano = int(input('Digite um ano inicial: '))
while ano < 1582 or ano > 2022:
    print('O ano digitado deve ser maior que 1582 e menor que 2022.')
    ano = int(input('Digite um ano inicial: '))
ano_aux = ano
count = 0
while ano_aux < 2022:
    if ano_aux % 4 == 0 and ano_aux % 100 != 0 or ano_aux % 400 == 0:
        print('O ano', ano_aux, ' é bissexto')
        count += 1
    ano_aux += 1
print('Houve', count, 'ano(s) bissexto(s).')