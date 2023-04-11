import requests

from flask import jsonify

url = "http://127.0.0.1:5000/requisicao"

def realizar_solicitacao():
    while True:
        mat = str(input("Insira uma matrícula "))
        equip = str(input("Insira um equipamento "))
        defe = str(input("Insira um defeito "))
        set = str(input("Insira um setor "))
        obj = {
            "mat": mat,
            "equip": equip,
            "def": defe,
            "set": set
        }
        r = requests.post(url, obj)
        print(r.text)
        opc = str(input("Deseja fazer uma nova solicitação? Y/N"))
        opc = opc.upper()
        if opc == "N":
            break
        
if __name__ == "__main__":
    realizar_solicitacao()

