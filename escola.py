# Trabalhando com IF e testes
tipoEscola = input("Tipo do colegio: \n [1] Publico \n [2] Paticular \n Resposta: ")
freqAluno = input("Qual a frequencia do aluno?")
nomeAluno =input("Qual o nome do Aluno: ")
mediaAluno =int(input("Qual a media do Aluno: "))
#mediaEscola =input("Media de corte da Escola: ")
mediaEscola = 7
freqAluno = int(freqAluno)


if tipoEscola == "2" :
    print("----- Colegio Particular -----")
    if mediaAluno >= mediaEscola and freqAluno >= 70 :
        print("Aprovado")
    else:
        print("reprovado")

if tipoEscola == "1" :
    print("-----Colegio Publico-----")
    if mediaAluno >= mediaEscola or freqAluno >= 60 :
        print("Aprovado")
    else: 
        print("Reprovado")
        