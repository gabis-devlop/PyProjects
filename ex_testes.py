class estoque:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
    
carro1 = estoque("Volkswagen", "Gol", 2021)
carro2 = estoque("Chevrolet", "Onix", 2022)
carro3 = estoque("Ford", "Ka", 2020)
carro4 = estoque("Fiat", "Uno", 2019)
carro5 = estoque("Renault", "Kwid", 2021)

carro1.descricao()
carro2.descricao()
carro3.descricao()
carro4.descricao()
carro5.descricao()