from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/consultar_ibge/<string:nome>", methods =['GET'])
def consultar(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?nome={nome}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)
