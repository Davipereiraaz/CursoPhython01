import json, requests

pesquisa = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/davi")

dados_json = json.loads(pesquisa.text)

print(dados_json[0]['res'][0])