class Bicicleta: #criação de classe, keyword e o nome da classe

 
    def __init__(self, cor, modelo, ano, valor, aro=18):    #inicialização dos atributos: define um METODO construtor e seus valores
        self.cor = cor #atributos
        self.modelo = modelo #atributos
        self.ano = ano #atributos
        self.valor = valor #atributos
        self.aro = aro
    
    def buzinar(self): #atribuindo comportamentos, definir o metodo usando def METODO e argumento (self)
        print("Plim plim")

    def parar(self):
        print("Parando bike...")
        print("Bike Parada!")

    def correr(self):
        print("vrummm vrumm...")
    
    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, mode={self.modelo}, ano={self.ano}, valor={self.valor}" FORMA DE CHAMAR O METODO, PORÉM TRABALHO E NECESSÁRIO ATUALIZAR SEMPRE QUE UM NOVO ARGUMENTO FOR INSERIDO

    #MELHOR FORMA DE EXPOR UM METODO, VISTO QUE NÃO SERÁ NECESSÁRIO ATUALIZAÇÃO, CASO SEJA INCLUIDO UM NOVO ARGUMENTO
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# b1 = Bicicleta("Vermelha", "caloi", 2022, 600)
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2)  # b2.buzinar()
print(b2.cor)
print(b2)