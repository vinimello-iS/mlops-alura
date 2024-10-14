import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("casas.csv")

colunas = ["tamanho", "preco"]
df = df[colunas]

X = df.drop("preco", axis=1)
y = df.preco

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)
