import requests

cep = "05886090"

url = f"https://viacep.com.br/ws/{cep}/json"
resposta = requests.get(url)
print(resposta)
dado = resposta.json()
print(dado)