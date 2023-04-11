from random import randrange
from datetime import date, timedelta
from flask import request, redirect


from flask import Flask, make_response, jsonify
from bd import tecnicos, servicos

app = Flask(__name__)

def get_hora():
    hora = f"{randrange(8, 17)}:{randrange(0, 59)}"
    return hora

def get_data():
    data_atual = date.today()
    data_servico = data_atual + timedelta(days=randrange(1, 3))
    return data_servico

@app.route("/requisicao", methods=["POST"])
def set_requisicao():
    if len(tecnicos) > 0:
        servico = request
        print(servico)
        servicos.append(servico)
        print(servicos)
        url = '/tecnicos/accept'
    else:
        url = '/tecnicos/error'

    return redirect(url)

@app.route("/tecnicos/accept", methods=["GET"])
def get_tecnicos():
    res = f"O técnico {tecnicos.pop(0)} irá realizar o serviço às {get_hora()} do dia {get_data()}"
    return res

@app.route("/tecnicos/error", methods=["GET"])
def not_get_tecnicos():
    res = "Nenhum técnico disponível"
    return res

app.run()