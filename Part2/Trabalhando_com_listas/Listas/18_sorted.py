# linguagens = ["python", "js", "c", "java", "csharp"]

# print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
# print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

lista = list(range(0, 100, 2))
lista = [n**2 
         if n > 6 
         else n for n in range(10) if n % 2 == 0]

print(lista)

