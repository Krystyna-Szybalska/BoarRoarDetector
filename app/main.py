from datetime import datetime
from flask import Flask, abort
from flask import request
from werkzeug.utils import secure_filename
import requests
from app.utils import AnimalType

app = Flask(__name__)

@app.route("/API/sensor/<sensor_id>/data", methods=['POST'])

def send_alert(sensor_id):
    api_key_from_sensor = request.headers.get('x-Api-Key')
    service_api_key = '1a87479852d0471881df50cb39e33283'
    if api_key_from_sensor != service_api_key:
        abort(403)

    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))

        # if dane są ok - wyjasnic jak dzialaloby ai

        Headers = { 'x-Api-Key': service_api_key}
        json = { 'detected_at': datetime.now().isoformat(), 'detected_animal': AnimalType.Boar.name}
        request_info = requests.post(f'http://localhost:5016/api/sensors/{sensor_id}/data', json=json, verify=False, headers=Headers)
        return 'sound file uploaded successfully '

app.run()

