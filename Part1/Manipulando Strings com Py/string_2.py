nome = "John"
idade = 24
profissao = "Analista"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s \nidade: %d" % (nome, idade))

print("Nome: {} \nidade: {}".format(nome, idade))

print("Nome: {1} \nidade: {0}".format(nome, idade))

print("Nome: {nome} \nidade: {idade}".format(**dados))

print(f"Nome: {nome} \nIdade: {idade} \nSaldo: {saldo:.2f}")

  