# saldo = 2000.0
# saque = float(input('Informe o valor do saque: '))

# if saldo >= saque:
#     print('Realizando o saque')

# # if saldo < saque:
# #     print('Saldo insuficiente')
# else:
#     print('Saldo Insuficiente')


# opcao = int(input("Informe uma opão: [1] Sacar \n [2] Extrato: "))

# if opcao == 1:
#     valor = float(input("Informe a quantia para o saque: "))

# elif opcao == 2:
#     print("Exibindo o Extrato ... ")

# else:
#     sys.exit("Opção Inválida")


MAIOR_IDADE = 18
IDADE_ESPECIAL = 15

idade = int(input("Informe sua idade: "))
            
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
# if idade < MAIOR_IDADE:
#     print("Menor de idade, não pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Permitido fazer somente aulas teóricas")
else:
    print("Menor de idade, não pode tirar CNH")



