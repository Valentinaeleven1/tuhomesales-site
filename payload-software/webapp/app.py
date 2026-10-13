from flask import Flask, jsonify, render_template, request
import datetime
import logging
import os
import sys
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from gps_reader import GPSReader
from signal_scanner import SignalScanner
from target_estimator import TargetEstimator

app = Flask(__name__)
config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

gps_reader = GPSReader(config.get('gps', {}))
scanner = SignalScanner(config.get('signal', {}))
estimator = TargetEstimator(config.get('target_estimation', {}))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    gps_data = gps_reader.get_position()
    signal_data = scanner.scan()
    mode = request.args.get('mode', 'both')
    estimate = estimator.estimate(signal_data.get('value'), mode=mode)
    return jsonify({
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'gps': gps_data,
        'signal': signal_data,
        'target_estimate': estimate,
    })

@app.route('/start', methods=['POST'])
def start():
    return jsonify({'status': 'started'})

@app.route('/stop', methods=['POST'])
def stop():
    return jsonify({'status': 'stopped'})

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run the rescue payload dashboard')
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind the web server')
    parser.add_argument('--port', type=int, default=5000, help='Port to bind the web server')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    app.run(host=args.host, port=args.port)
