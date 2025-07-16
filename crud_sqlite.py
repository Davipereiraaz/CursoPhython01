import sqlite3 

# Primeiro vamos nos conectar ao banco de dados (ou criar um novo se nao existir)

def conectar_banco():
    conexao = sqlite3.connect('exemplo02.db') #Nome de banco de dados
    return conexao

# Criar tabela no novo banco exemplo.db
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )     
''')
    conexao.commit()
    conexao.close()
# inserir dados na tabela 
def inserir_usuario(campo_nome, campo_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade) VALUES (?,?)''' ,(campo_nome, campo_idade))
    conexao.commit()
    conexao.close()

    #Ler dados de banco
def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

# Atualizar dados do banco
def atualizar_usuario(id, novo_nome, nova_idade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?,
        idade = ?
        WHERE id = ?
''' , (novo_nome, nova_idade, id))
    conexao.commit()
    conexao.close()
 
#Excluir dados do banco
def excluir_usuario(id):  
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios WHERE ID = ?
''', (id,))
    conexao.commit()
    conexao.close()

# Exemplos de uso das Funções CRUD
# criar a tabela (execute apenas uma unica vez)
criar_tabela()

# inserir alguns dado!
inserir_usuario('Caio', 31)
inserir_usuario('Jesreel', 21)
inserir_usuario('Eloara', 42)
inserir_usuario('Alice', 23)
inserir_usuario('Emily', 20)
inserir_usuario('Davi', 18)
inserir_usuario('Andressa', 51)

# Ver os dados cadastrados
print('Ver dados antes de serem atualizados ')
listar_usuarios()

#Atualizar a idade de um usuario!
atualizar_usuario(6, 'Davi Pereira', 17)

#Listar usuarios após a atualização
print('\n Lista de usuarios atualizada')
listar_usuarios()

#Excluir usuario
excluir_usuario(7)

# Listar usuarios após a exclusão
print('/n Lista de usuarios atualizadas')
listar_usuarios()

