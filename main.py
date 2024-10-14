from flask import Flask
from textblob import TextBlob
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return "Minha primeira API"


@app.route("/sentimento/<frase>")
def sentimento(frase):
    tb = TextBlob(frase)
    polaridade = tb.sentiment.polarity
    return f"polaridade: {polaridade}"


app.run(debug=True)
