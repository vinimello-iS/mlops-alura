from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
import pickle

colunas = ["tamanho", "ano", "garagem"]
modelo = pickle.load(open("modelo.sav", "rb"))

app = Flask(__name__)
app.config["BASIC_AUTH_USERNAME"] = "Vinicius"
app.config["BASIC_AUTH_PASSWORD"] = "123"

basic_auth = BasicAuth(app)


@app.route("/")
def home():
    return "Minha primeira API"


@app.route("/sentimento/<frase>")
def sentimento(frase):
    tb = TextBlob(frase)
    polaridade = tb.sentiment.polarity
    return f"polaridade: {polaridade}"


@app.route("/cotacao/", methods=["POST"])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])

    return jsonify(preco=preco[0])


app.run(debug=True)
