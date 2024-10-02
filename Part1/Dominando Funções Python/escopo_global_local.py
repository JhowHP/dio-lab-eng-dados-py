salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(5)
    print(f"Lista aux = {lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista) #2500
print(salario_com_bonus)
print(lista)


# def salario_extra(extra):
#     salario = 2300
#     salario += extra
#     return salario

# salario_com_extra = salario_extra(525)

# print(salario_com_extra)