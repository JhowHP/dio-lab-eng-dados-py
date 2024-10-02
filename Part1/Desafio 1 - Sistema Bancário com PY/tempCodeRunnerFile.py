menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[f] Sair

=>   """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

    elif opcao == "s":
        print("Sacar")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "f":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    