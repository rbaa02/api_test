from flask import Flask, jsonify
import pandas as pd


app = Flask(__name__)


@app.route('/')
def f_homepage():
    return 'HOMEPAGE_API'


@app.route('/vendas', methods=['GET'])
def f_vendas():
    tabela = pd.read_csv('dados.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


app.run(port=80)
