from flask import Flask, jsonify, request

app = Flask(__name__)

data = [

        {"placa": "qhg984", "fecha": "18/04/22 9:55:19", "codigo": "T00056470"},
        {"placa": "gng550", "fecha": "19/04/22 7:25:30", "codigo": "T00000001"},
        {"placa": "fff984", "fecha": "20/04/22 6:55:19", "codigo": "T00000021"},
        {"placa": "ggg999", "fecha": "22/04/22 8:55:19", "codigo": "V00000001"}

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

@app.route("/carros/<string:placa>", methods=["PUT"]) #Hacer la prueba con insomnia
def update_carros(placa):
    counter = 0
    for carro in data:
        if carro["placa"] == placa:
            carro["fecha"] = request.json["fecha"]
            carro["codigo"] = request.json["codigo"]

            print(data[counter]["placa"])
            return jsonify({"responsse":carro})

        counter =+1
    return jsonify({"msg": "Vehiculo no encontrado"})

@app.route("/carros", methods=["POST"])
def add_carro():
    new_carro = {
            "placa": request.json["placa"],
            "fecha": request.json["fecha"],
            "codigo": request.json["codigo"]
            }

    data.append(new_carro)
    return jsonify({

        "mensaje": "carro nuevo agregado correctamente, enviando data actual",
        "carros": data

        })

@app.route("/carros/<string:placa>", methods=["DELETE"])
def delete_carr(placa):
    counter = 0
    for carro in data:
        if carro["placa"] == placa:
            print(data[counter]["placa"])
            data.remove(carro)
            return jsonify({"mensaje":"carro eliminado", "responsse":carro})

        counter =+1

    return jsonify({"mensaje":"Carro no encontrado, abortada accion de borrado"})





# Usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(users)

@app.route("/usuarios/<string:id>", methods=["PUT"])
def update_usuario(id):
    counter = 0
    for usuario in users:
        if usuario["codigo"] == id:
            usuario["nombres"] = request.json["nombres"]
            usuario["edad"] = request.json["edad"]
            usuario["rol"] = request.json["rol"]

            print(users[counter]["codigo"])
            return jsonify({"responsse":users})

        counter =+1
    return jsonify({"msg": "Usuario no encontrado"})

@app.route("/usuarios", methods=["POST"])
def add_new_user():
    new_user = {
            "codigo": request.json["codigo"],
            "nombres": request.json["nombres"],
            "rol": request.json["rol"],
            "edad": request.json["edad"]

            }

    users.append(new_user)
    return jsonify({

        "mensaje": "usuario nuevo agregado correctamente, enviando catalogo actual",
        "usuarios": users

        })

@app.route("/usuarios/<string:id>", methods=["DELETE"])
def delete_user(id):
    counter = 0
    for usuario in users:
        if usuario["codigo"] == id:
            print(users[counter]["codigo"])
            users.remove(usuario)
            return jsonify({"mensaje":"usuario eliminado", "responsse":usuario})

        counter =+1

    return jsonify({"mensaje":"Usuario no encontrado, abortada accion de borrado"})






if __name__ == '__main__':
    app.run(debug=True)
