# Calculadora Básica em Python


# função que gera o texto ce introdução

def intro():

    return '''
 .d8888b.           888                   888               888                          
d88P  Y88b          888                   888               888                          
888    888          888                   888               888                          
888         8888b.  888  .d8888b 888  888 888  8888b.   .d88888  .d88b.  888d888 8888b.  
888            "88b 888 d88P"    888  888 888     "88b d88" 888 d88""88b 888P"      "88b 
888    888 .d888888 888 888      888  888 888 .d888888 888  888 888  888 888    .d888888 
Y88b  d88P 888  888 888 Y88b.    Y88b 888 888 888  888 Y88b 888 Y88..88P 888    888  888 
 "Y8888P"  "Y888888 888  "Y8888P  "Y88888 888 "Y888888  "Y88888  "Y88P"  888    "Y888888 

---Feito por: Davi com amor---


'''

# função que gera o menu inicial
def mostrar_menu() :
    return ''' 
        [1] ou [+] para
        [2] ou [-] para
        [3] ou [*] para
        [4] ou [/] para
        [5] para Sair
        (ou digite sua opção: Somar / Substituir / Multiplicar / Dividir / Sair )
       ''' 

# função que le os valores
def ler_valores() :
    valor01 = int(input('Insira o primeiro valor: '))
    valor02 = int(input('Insira o segundo valor: '))
    return valor01, valor02

def somar(a ,b) :
    return a + b 
def subtrair(a ,b) :
    return a - b 
def dividir(a ,b) :
    return a / b
def multiplicar(a ,b) :
    return a * b

#função para permanecer ou sair do programa
def desejacontinuar() :
    print('''
        [1] Não, desejo sair!
        [2] Sim, desejo realizar outro calculo
    ''')
    opcao = input('Deseja realizar outra conta? ')
    return opcao != '1' 

#looping Principal
executar = True
print(intro())
while executar :
    print(mostrar_menu())
    operador = input ('Qual a sua opção?: ').strip().lower()

    if operador in ['5', 'sair']:
        print('Obrigado por usar a melhor calculadora')
        break

    v01, v02 = ler_valores()

    if operador in ['1','+', 'somar'] :
        resultado = somar(v01, v02)
    elif operador in ['2','+', 'subtrair'] :
        resultado = subtrair(v01, v02)    
    elif operador in ['3','+','multiplicar'] :
        resultado = multiplicar(v01, v02)
    elif operador in ['4','+', 'dividir'] :
        resultado = dividir(v01, v02)
    else: 
        print('Opção invalida. Tente novamente.')
        continue

    print('Resultado é: ' + str(resultado))
    executar = desejacontinuar()