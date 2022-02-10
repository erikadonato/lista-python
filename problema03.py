data1dia = int(input('Digite o dia da data1:'))
data1mes = int(input('Digite o mês da data1:'))
data1ano = int(input('Digite o ano da data1:'))
data2dia = int(input('Digite o dia da data2:'))
data2mes = int(input('Digite o mês da data2:'))
data2ano = int(input('Digite o ano da data2:'))
if data1dia == data2dia and data1mes == data2mes and data1ano == data2ano:
    print('As datas são iguais!')
elif data1ano > data2ano:
    print('A data 1 é maior!')
elif data1ano == data2ano and data1mes > data2mes:
    print('A data 1 é maior!')
elif data1ano == data2ano and data1mes == data2mes and data1dia > data2dia:
    print('A data 1 é maior!')
else: 
    print('A data 2 é maior!')