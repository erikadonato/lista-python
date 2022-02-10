soma = media = maior = menor = contador = indicemenornota = indicemaiornota = 0
for x in range(1, 6):
    nota = float(input('Digite uma nota: '))
    soma += nota
    contador += 1
    media = soma/contador
    if contador == 1:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
            indicemaiornota = contador-1
        if nota < menor:
            menor = nota
            indicemenornota = contador-1
print('Média:', round(media, 1))
print('Menor: nota',indicemenornota, '=', menor)
print('Maior: nota', indicemaiornota, '=', maior)
