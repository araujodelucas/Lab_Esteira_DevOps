from flask import Flask, jsonify, request

app = Flask(__name__)

#lista para receber os comentários
comentarios = []

#consultando todos os comentários
@app.route('/consultar', methods=['GET'])
def home():
    return jsonify(comentarios), 200

#inserindo um novo comentário
@app.route('/comentar', methods=['POST'])
def comentar():
    inserir = request.get_json()
    comentarios.append(inserir) #salvando o dado em memória
    return jsonify(inserir), 201

#habilitando o modo debug
if __name__ == '__main__':
    app.run(debug=True)