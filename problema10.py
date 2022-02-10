matriz = []
traco = 0.0
dimensao = int(input('Digite a dimensão da matriz quadrada:'))
n_linhas = n_colunas = dimensao

for i in range(n_linhas):
    linha = []
    for j in range(n_colunas):
        valor = float(input(f'Elemento {i} x {j}: '))
        linha.append(valor)
    matriz.append(linha)
print('Matriz digitada:')
for i in range(n_linhas):
    for j in range(n_colunas):
       print(f'[{matriz[i][j]:^{dimensao}}]', end='')
       if i == j: 
           traco+= matriz[i][j]
    print()
print('Traço da matriz: ', traco)