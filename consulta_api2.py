import json, requests

nome = input('Qual o seu nome?')
localidade = 0

while localidade < 1 or localidade > 2:
    localidade = int(input('Você deseja selecionar uam localidade? \n [1] Sim \n [2] Não \n'))

if localidade == 1 :
    uf = input('Qual Uf deseja buscar? \n [35] SP \n [33] RJ \n [31] MG \n [43] RS \n [53] DF \n')
    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/davi?{nome}localidade={uf}')

if localidade == 2 :
    resultado = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')

print('''
    [1] - 1930
    [2] - 1930 até 1940
    [3] - 1940 até 1950
    [4] - 1950 até 1960
    [5] - 1960 até 1970 
    [6] - 1970 até 1980
    [7] - 1980 até 1990
    [8] - 1990 até 2000
    [9] - 2000 até 2010 
''')   
tempo = int(input('Selecione o periodo: ')) -1
dados = json.loads(resultado.text)
print(dados[0]['res'][tempo])
    