curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

exp = curso is nome_curso
print(exp)
exp2 = curso is not nome_curso
print(exp2)

exp3 = saldo is not limite
print(exp3)