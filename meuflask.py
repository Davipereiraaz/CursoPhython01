from flask import Flask, render_template 

#Criação do app flask
app = Flask(__name__)

#Rota da pagina Principal
@app.route('/')
def home():
    return "<h1>Bem vindo a minha API </h1>"

# Rota da pagina sobre
@app.route('/sobre')
def sobre():
    return "<h1> Criado por Davi </h1>"

# Rota com variaveis na URL
@app.route('/ola/<nome>')
def ola(nome):
    return f"<h1>Olá, {nome}!</h1><br/><h2>Bem vindo a minha pagina pessoal</h2><a href='http://www.google.com'>Google</a>"

# Iniciar o servidor 
if __name__ == '__main__' :
    app.run(debug=True)