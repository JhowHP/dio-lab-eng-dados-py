######## SISTEMA DE BANCO #############

# conta_normal = 5000
# cheque_especial = 1000
# conta_universitaria = 2500
# saldo = 5000
# saque = float(input("Informe o valor do seu saque: "))

conta_normal = 1
conta_universitaria = 2

saldo = 2000
# saque = 2500
cheque_especial = 450

conta = int(input("Informe seu tipo de conta: \n [1] Conta Normal \n [2] Conta Universitária\n ------------------------------ \n"))
saque = float(input("Informe o valor do saque: \n"))
print(f"A conta selecionada: {conta}")

if conta_normal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do chque especial!")
    else:
        print("Sem saldo! Não foi possível realizar o saque!")

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu o tipo de conta!")