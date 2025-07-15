#Palavra trabalhando com Loopings

palavra = "garrafinha"
contador = 8
print("Palavra Escolhida: " , palavra)
for letra in palavra :
    print(contador , " - " , letra) 
    contador = contador + 1

cidades = ['São Paulo', 'Santos', 'Guaruja', 'Praia Grande', 'Campinas', 'Londres' ]

for cidade in cidades :
    print(cidade)    

print(cidades[0])  

print("--------While--------")

botaoExecutar =  True #valor boolean
contador = 0
while botaoExecutar : 
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False

compras = ['Pães', 'Ovos', 'Frutas', 'Chocolate', 'Azeite', 'Carne', 'Peixe', 'Arroz']
contador = 1
for itens in compras :
    # print('[',contador, ']',  itens)
    print('[' + str(contador) + '] ' +  itens + '\n')
    contador = contador + 1
