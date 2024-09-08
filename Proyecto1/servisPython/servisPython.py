import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_info():
    data = request.get_json()
    with open('/logs/rust_requests.log', 'a') as log_file:
        json.dump(data, log_file)
        log_file.write('\n')
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
