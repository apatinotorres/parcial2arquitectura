from flask import Flask, jsonify, request

app = Flask(__name__)

data = [

        {"placa": "QHG984", "fecha": "18/04/22 9:55:19", "codigo": "T00056470"},
        {"placa": "GNG550", "fecha": "19/04/22 7:25:30", "codigo": "T00000001"},
        {"placa": "FFF984", "fecha": "20/04/22 6:55:19", "codigo": "T00000021"},
        {"placa": "GGG999", "fecha": "22/04/22 8:55:19", "codigo": "V00000001"}

        ]

users = [
        {"codigo": "T00056470", "nombres": "Antonio Jose Patiño Torres", "edad": "21", "rol": "estudiante"},
        {"codigo": "T00000001", "nombres": "Tomas David Patiño Torres",  "edad": "18", "rol": "profesor"},
        {"codigo": "T00000021", "nombres": "Usuario no def",             "edad": "35", "rol": "administrativo"},
        {"codigo": "V00000001", "nombres": "Prueba",                     "edad": "50", "rol": "visitante"  }
        ]

@app.route("/")
def homepage():
    return "hola mundo!"



# carros
@app.route("/carros", methods=["GET"])
def obtener_carros():
    return jsonify(data)

@app.route("/carros/<string:placa>", methods=["PUT"])
def update_carros(placa):
    carro_encontrado = [carro for carro in data if data["placa"] == placa]
    if (len(carro_encontrado) > 0):
        return jsonify({'Vehiculo': carro_encontrado[0]})
    return jsonify({"msg": "Vehiculo no encontrado"})




# Usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(users)




if __name__ == '__main__':
    app.run(debug=True)
