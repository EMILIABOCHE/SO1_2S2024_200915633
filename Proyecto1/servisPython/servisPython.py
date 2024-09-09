 from flask import Flask, request, jsonify
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)

# Archivo JSON donde se guardarán los logs
LOG_FILE = '/app/logs/logs.json'  # Usaremos un volumen para que este archivo sea accesible

# Verificamos si el archivo de logs existe, si no, lo creamos vacío.
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        json.dump([], f)


# Ruta para recibir logs del servicio de Rust
@app.route('/log', methods=['POST'])
def log_process():
    log_data = request.get_json()

    # Cargar los logs actuales
    with open(LOG_FILE, 'r') as f:
        logs = json.load(f)

    # Agregar nuevo log con timestamp
    log_data['timestamp'] = datetime.now().isoformat()
    logs.append(log_data)

    # Guardar logs de nuevo en el archivo
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=4)

    return jsonify({"status": "log added"}), 200


# Ruta para generar gráficas a partir de los logs
@app.route('/generate-graphs', methods=['GET'])
def generate_graphs():
    # Cargar los logs
    with open(LOG_FILE, 'r') as f:
        logs = json.load(f)

    if len(logs) == 0:
        return jsonify({"status": "No logs to generate graphs"}), 400

    # Generar gráficas usando matplotlib
    generate_memory_usage_graph(logs)
    generate_cpu_usage_graph(logs)

    return jsonify({"status": "graphs generated"}), 200


# Función para generar gráfica de uso de memoria
def generate_memory_usage_graph(logs):
    pids = [log['pid'] for log in logs]
    memory_usage = [log['memory_usage'] for log in logs]

    plt.figure(figsize=(10, 6))
    plt.bar(pids, memory_usage, color='blue')
    plt.xlabel('PID')
    plt.ylabel('Memory Usage (MB)')
    plt.title('Memory Usage by Process ID')
    plt.savefig('/app/logs/memory_usage_graph.png')
    plt.close()


# Función para generar gráfica de uso de CPU
def generate_cpu_usage_graph(logs):
    pids = [log['pid'] for log in logs]
    cpu_usage = [log['cpu_usage'] for log in logs]

    plt.figure(figsize=(10, 6))
    plt.bar(pids, cpu_usage, color='red')
    plt.xlabel('PID')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage by Process ID')
    plt.savefig('/app/logs/cpu_usage_graph.png')
    plt.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
