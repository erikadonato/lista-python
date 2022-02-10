base = float(input('Digite a base do triângulo:'))
while base <= 0:
    print('Digite um valor positivo!')
    base = float(input('Digite a base do triângulo:'))
altura = float(input('Digite a altura do triângulo:'))
while altura <= 0: 
    print('Digite um valor positivo!')
    altura = float(input('Digite a altura do triângulo:'))
area = base * altura / 2
print('A área do triângulo é', area)