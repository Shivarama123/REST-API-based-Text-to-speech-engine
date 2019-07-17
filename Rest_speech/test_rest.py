import threading
from datetime import time
from flask import Flask, jsonify, request
import pytts

app = Flask(__name__)

app_thread = None
PORT = 5111

@app.route('/api/pytts/text/<string:phrase>')
def run_pytts(phrase):
    try:
        pytts.speak_phrase(phrase)
        return jsonify({'data': 'SUCCESS'})
    except:
        return jsonify({'data': 'FAIL'})

def start_rest_service():
    app.run(port=PORT)


def start_rest_thread():
    global app_thread
    app_thread = threading.Thread(name='start_rest_service', target=start_rest_service)
    app_thread.start()