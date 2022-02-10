while True:
    
    angulo = float(input("Digite o ângulo desejado: "))
    angulo_inicial = angulo
    reduzido = angulo
    while(angulo > 360):
        angulo -= 360

    if (angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360):
        print("O ângulo ",round(angulo_inicial,1)," não possui quadrante determinado.")

    if(angulo>0 and angulo<90):
        print("O ângulo",round(angulo_inicial,1),"graus pode ser reduzido a", round(angulo,1), "graus e está no quadrante 1.")

    if(angulo>90 and angulo<180):
        print("O ângulo",round(angulo_inicial,1),"graus pode ser reduzido a", round(angulo,1), "graus e está no quadrante 2.")

    if(angulo>180 and angulo<270):
        print("O ângulo",round(angulo_inicial,1),"graus pode ser reduzido a", round(angulo,1), "graus e está no quadrante 3.")
    if(angulo>270 and angulo<360):
        print("O ângulo",round(angulo_inicial,1),"graus pode ser reduzido a", round(angulo,1), "graus e está no quadrante 4.")

