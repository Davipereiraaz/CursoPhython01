# Introdução a orientação a objeto
# exmeplo simples 01

class carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0 # o carro começa parado

# acelerar o carro aumentando sua velocidade com incrementos personalizados
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f' O carro {self.modelo} da cor {self.cor} acelerou para {self.velocidade} KM/h')

# Parar o carro , reduzindo sua velocidade para 0
    def parar(self):
        self.velocidade = 0
        print(f' O carro {self.modelo} da cor {self.cor} parou bruscamente') 

    def desacelerar(self, decremento):
        self.velocidade -= decremento
        print(f' O carro {self.modelo} da cor {self.cor} desacelerou para {self.velocidade} KM/h') 


#Cria um objeto carro
meu_carro01 = carro('fusca', 'amarelo')
meu_carro02 = carro('sj', 'preto')


meu_carro01.acelerar(40)
meu_carro02.acelerar(20)
meu_carro01.desacelerar (5)
meu_carro02.parar()


 # Acelerar o carro a 20KM/h
#Acelerar o carro a 50KM/h
#Parar o carro 