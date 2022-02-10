frase = str(input('Digite uma frase:'))
palavra = str(input('Digite uma palavra:'))
print('Frase digitada:',frase)
print('Palavra digitada:',palavra)
for i, p in enumerate(frase):
    if frase[i:i + len(palavra)] == palavra:
        print('{} aparece na posição {}'.format(palavra, i))