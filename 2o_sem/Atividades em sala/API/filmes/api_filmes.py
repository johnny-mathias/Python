import banco
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/filmes", methods=['GET'])
def recupera_filmes():
    return (banco.filmes, 200)

@app.route("/filmes", methods=['POST'])
def cria_filme():
    filme = request.json
    #poderia fazer uma RN: nao existem dois filmes com o mesmo nome
    banco.filmes.append(filme)
    return (filme, 201)

@app.route("/filmes", methods=['PUT'])
def atualiza_filmes():
    filme = request.json
    achou = False
    
    i = 0
    while i < len(banco.filmes):
        if filme['titulo'] == banco.filmes[i]['titulo']:
            banco.filmes[i] = filme
            achou = True
        i+= 1
        
    if not achou:
        info = {"title": "not found", "status": 404}
        return info, 404
    return (filme, 201)

app.run(debug=True)