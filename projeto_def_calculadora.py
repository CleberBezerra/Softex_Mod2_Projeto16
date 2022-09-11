def def_calculadora(num1, num2, operacao):
    if (operacao == 1):
        resultado = num1 + num2
    elif (operacao == 2):
        resultado = num1 - num2
    elif (operacao == 3):
        resultado = num1 * num2
    elif (operacao == 4):
        resultado = num1 / num2
    else:
        resultado = 0

    return resultado

resul = def_calculadora(3, 9, 3)
print("O resultado é: ",resul)