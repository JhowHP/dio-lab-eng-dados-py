def calcular_total(numeros):
    return sum(numeros)


def retornar_antecessor_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá mundo")

print(calcular_total([10, 20, 34]))
print(retornar_antecessor_sucessor(10)) # (9, 11)
print(func_3())