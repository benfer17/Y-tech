from flask import Flask, render_template, jsonify
import sqlite3
import random



import time

app = Flask(__name__)

# Pines del sensor HC-SR04


def medir_distancia():
    return round(random.uniform(5, 100), 2)  # simula distancia entre 5 y 100 cm

    duracion = fin - inicio
    distancia = (duracion * 34300) / 2  # en cm
    return round(distancia, 2)

def get_mediciones():
    conn = sqlite3.connect("database/sensoalertas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vista_ultimas_mediciones LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows


#_____________________________________________________________________________
# @app.route('/data', methods=['POST'])
# def recibir_datos():
#     data = request.get_json()

#     if not data:
#         return jsonify({
#             "status": "error",
#             "mensaje": "No se recibió JSON válido"
#         }), 400

#     # Extraer valores
#     distancia = data.get("distancia")
#     nivel = data.get("nivel")

#     # Mostrar en consola
#     print("=== Datos recibidos del ESP32 ===")
#     print(f"Distancia: {distancia} cm")
#     print(f"Nivel: {nivel} %")
#     print("=================================")

#     # Responder con los mismos datos
#     return jsonify({
#         "status": "ok",
#         "mensaje": "Datos recibidos correctamente",
#         "distancia": distancia,
#         "nivel": nivel
#     }), 200

#__________________________________________________________________________________


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/mediciones")
def mediciones():
    data = get_mediciones()
    return jsonify(data)

@app.route("/api/alertas")
def alertas():
    conn = sqlite3.connect("database/sensoalertas.db")
    cursor = conn.cursor()

    # Simula alertas: si hay valores de distancia < 10 cm en las últimas 10 lecturas
    cursor.execute("""
        SELECT sensores.nombre, mediciones_real.valor, mediciones_real.fecha_hora
        FROM mediciones_real
        JOIN sensores ON sensores.id_sensor = mediciones_real.id_sensor
        WHERE valor < 10
        ORDER BY fecha_hora DESC
        LIMIT 5
    """)
    
    alertas = cursor.fetchall()
    conn.close()
    return jsonify(alertas)
@app.route("/api/simular_alarma")
def simular_alarma():
    conn = sqlite3.connect("database/sensoalertas.db")
    cursor = conn.cursor()

    # Insertar en mediciones_real un valor < 10
    cursor.execute("""
        INSERT INTO mediciones_real (id_sensor, id_medicion, valor, fecha_hora)
        VALUES (2, 1, 5.0, datetime('now'))
    """)
    conn.commit()
    conn.close()
    return jsonify({"status": "alarma simulada"})


@app.route("/api/distancia")
def distancia():
    valor = medir_distancia()
    return jsonify({"distancia": valor})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
