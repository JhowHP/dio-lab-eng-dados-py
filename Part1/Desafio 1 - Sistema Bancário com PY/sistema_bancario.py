menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[f] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

# DEPOSITO

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: \n"))
        

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("""
            Depósito Realiazdo
              """)

        else:
            print("\nOperação falhou: O valor informado é inválido.")


       

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: \n"))
# SACAR

#VERIFICAÇÕES 

        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite
        
        execedeu_saques = numeros_saques == LIMITE_SAQUES

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif execedeu_limite:
            print("Operação falhou! O valor de saque execedeu o limite permitido")

        elif execedeu_saques:
            print("Operação falhou! Você execedeu o limite de saques diário.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numeros_saques += 1
            print("""
            Saque Realiazdo
              """)

            
        else:
            print("Operação falhou! O valor informado é inválido")


#EXTRATO

    elif opcao == "e":
        print("\n================= EXTRATO ===================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")


    elif opcao == "f":
        print("""
              
              Obrigado por utilizar nossos serviços
              
              """)
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    