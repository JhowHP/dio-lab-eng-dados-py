class Veiculos:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas


    def ligar_motor(self):
        print("Ligando motor...")
    


class Motocicleta(Veiculos):
    pass


class Carro(Veiculos):
    pass


class Caminhao(Veiculos):
    def __init__(self, cor, placa, numero_rodas,carregado):
        self.carregado = carregado
        super().__init__(cor,placa, numero_rodas)
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")



# moto = Motocicleta("Preta", "ABC-123", 2)
# moto.ligar_motor()

# carro = Carro("Branco", "XDX-123", 4)
# carro.ligar_motor()

caminhao = Caminhao("Roxo", "FDS-324", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()