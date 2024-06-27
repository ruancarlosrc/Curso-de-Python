class Bicicleta:
    def__init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

    def buzinar(self):
        print("plim plim....")
    
    def parar(self):
        print("parando bicicleta")
        print("bicicleta parada")
    
    def correr(self):
        print("vrummmm...")
    
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()