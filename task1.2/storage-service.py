import os, json, tempfile
from flask import Flask, request, jsonify, render_template
from flask_restful import Api

app = Flask(__name__)
api = Api()


STORAGE_PATH = os.path.join(tempfile.gettempdir(), 'storage.data')
PORT_SERVICE = 3000
HOST_SERVICE = '0.0.0.0'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/storage/json/all', methods=['GET'])
def get():
    with open(STORAGE_PATH, 'r') as f:
        m = json.load(f)
        return m

@app.route('/api/v1/storage/json/read', methods=['GET'])
def read():
    with open(STORAGE_PATH, 'r') as f:
        m = json.load(f)
        return jsonify(m.get(request.args['key']))

@app.route('/api/v1/storage/json/write', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')

    if os.path.isfile(STORAGE_PATH):
        if (content_type == 'application/json'):
            json_request = request.get_json()
            with open(STORAGE_PATH, 'r') as f:
                m = json.load(f)
                m.update(json_request)
            with open(STORAGE_PATH, 'w') as f:
                json.dump(m, f)
                return json_request
        else:
            return 'Content-Type not supported'
    else:
       json_request = request.get_json()
    with open(STORAGE_PATH, 'w') as f:
            json.dump(json_request, f)
            return json_request


if __name__ == '__main__':
    app.run(debug=True, port=PORT_SERVICE, host=HOST_SERVICE)