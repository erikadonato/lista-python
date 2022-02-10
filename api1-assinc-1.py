maioridade = menoridade = contador = 0
mediaaltura = maioraltura = menoraltura = aux_altura = contadoraltura = 0
produto = 1
while True:
    idade = int(input('Qual a idade da pessoa? '))
    if idade > 0:
        altura = float(input('Qual a altura da pessoa? '))
        while altura < 0:
            print('A altura é inválida!')
            altura = float(input('Qual a altura da pessoa? '))
        contador += 1
        if idade > 18:
            contadoraltura +=  1
            aux_altura += altura
            mediaaltura = aux_altura/contadoraltura
        if contador == 1:
            maioridade = menoridade = idade
            maioraltura = menoraltura = altura
        else:
            if idade > maioridade:
                maioridade = idade
            if idade < menoridade: 
                menoridade = idade
            if altura > maioraltura:
                maioraltura = altura
            if altura < menoraltura:
                menoraltura = altura
    else:
        print('Menor idade:', menoridade, 'anos')
        print('Maior idade:', maioridade, 'anos')
        print('Menor altura:', menoraltura, 'metros')
        print('Maior altura:', maioraltura, 'metros')
        print('Altura média dos adultos:', round(mediaaltura, 2), 'metros')
        break