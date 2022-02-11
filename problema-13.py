valor_disciplinas = int(input('Qual o número de disciplinas? '))
lista_notas = list()
disciplinas = dict()

for x in range(valor_disciplinas):
    disciplinas['nome'] = str(input('Qual o nome da disciplina? '))
    nota = str(input('Digite as 3 notas da disciplina separadas por vírgulas: ')).split(',')
    disciplinas['notas'] = []
    disciplinas['media'] = []
    for i in range(3):
        disciplinas['notas'].append(int(nota[i]))
    disciplinas['media'] = round(sum(disciplinas['notas'])/len(disciplinas['notas']), 1)
    lista_notas.append(disciplinas.copy())
for d in lista_notas: 
    print(disciplinas['nome'])
    for i in range(3): 
        print('Nota {}: {}'.format(i+1, disciplinas['notas'][i]))
    print('Média:',disciplinas['media'])