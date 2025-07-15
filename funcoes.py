#Entendendo Funções em Python
'''
def minhaFuncao() : 
    print("Olá Mundo")

minhaFuncao()
minhaFuncao()

alunos = ['Jesreel','Eloara', 'Emily','Alice', 'Andressa', 'Davi']
cursos = ['Python','PHP', 'SQL']

#trabalhando com variaveis de função
def minhaFuncaoMelhorada(animal, primaveras) :
    print('Você gosta de ' , animal, 'e ele tem' , primaveras , 'anos')

petCliente = input('Qual seu animal preferido?')
idadePet = input('Qual a idade do seu '+ petCliente )
minhaFuncaoMelhorada(petCliente, idadePet)
minhaFuncaoMelhorada('iguana' , '4')
'''



executar = True
while executar :
    anoNasc = int(input('Em que ano você nasceu? '))
    anoAtual = int(input('Em que anos estamos? '))
    idade = (anoAtual - anoNasc )
    print('Você tem: ', idade, 'anos')

    opcao = input('\n Deseja tentar novamente? \n [1]Sim \n [2]Não \n')
    if opcao == '2' :
        executar = False

 

print('----- Segundo Exercicio Usando Funções -----')

def calcular_idade() :        
    anoNsc = int(input('Em que ano você nasceu? '))
    anoAtl = (input('Em que anos estamos? '))
    idade = anoAtl - anoNsc
    print('Você tem ' + str(idade) + 'anos.')

def perguntarnovamente() :
        opcao = input('Deseja testar novamente? Sim ou Não')
        if opcao.lower() in ['sim', 's', 'sm', 'simm'] :
            iniciarprograma()
        else :
            print('Encerrando programa! Até mais')

def iniciarprograma() :
    calcular_idade()
    perguntarnovamente()
