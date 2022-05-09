from flask import Flask, render_template, request

import createDatabase

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/gravar", methods=["POST"])
def gravar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    preco = request.form["preco"]

    createDatabase.gravar(nome, categoria, preco)

    dados = createDatabase.consulta()

    return 'Os dados digitados foram salvos'


@app.route("/consultar")
def consultar():
    dados = createDatabase.consulta()
    return dados.to_html()


app.run(host="0.0.0.0", debug=True)
