def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def divisao(a, b):
    return a // b

def test(a, b):
    return a + 2 + b * 5

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é de {resultado}')


exibir_resultado(10, 20, somar)
exibir_resultado(10, 20, subtrair)
exibir_resultado(10, 20, divisao)
exibir_resultado(10, 20, test)


op = somar

print(op(1,23))