#!/usr/bin/env python3
import argparse
import csv
import datetime
import logging
import os
import signal
import sys
import time

import yaml
from gps_reader import GPSReader
from signal_scanner import SignalScanner

STOPPED = False


def handle_sigint(signum, frame):
    global STOPPED
    STOPPED = True


def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def ensure_directory(path):
    if not path:
        return
    os.makedirs(path, exist_ok=True)


def write_csv_header(path, headers):
    is_new = not os.path.exists(path)
    ensure_directory(os.path.dirname(path))
    if is_new:
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()


def append_csv(path, row, headers):
    with open(path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writerow(row)


def append_json(path, row):
    try:
        import json
        ensure_directory(os.path.dirname(path))
        if not os.path.exists(path):
            with open(path, 'w') as jf:
                json.dump([row], jf, indent=2)
        else:
            with open(path, 'r+') as jf:
                data = json.load(jf)
                data.append(row)
                jf.seek(0)
                json.dump(data, jf, indent=2)
                jf.truncate()
    except Exception as exc:
        logging.warning('Failed to append JSON: %s', exc)


def build_row(timestamp, gps_data, signal_data, mission_name):
    row = {
        'mission_name': mission_name,
        'timestamp': timestamp.isoformat(),
        'latitude': gps_data.get('latitude'),
        'longitude': gps_data.get('longitude'),
        'altitude': gps_data.get('altitude'),
        'fix_type': gps_data.get('fix_type'),
        'satellites': gps_data.get('satellites'),
        'signal_type': signal_data.get('type'),
        'signal_value': signal_data.get('value'),
        'signal_details': signal_data.get('details'),
    }
    return row


def parse_args():
    parser = argparse.ArgumentParser(description='Rescue payload logger for Raspberry Pi drone payload')
    parser.add_argument('--config', default='config.yaml', help='Path to config file')
    return parser.parse_args()


def main():
    signal.signal(signal.SIGINT, handle_sigint)
    signal.signal(signal.SIGTERM, handle_sigint)

    args = parse_args()
    config = load_config(args.config)

    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info('Starting payload logger')

    gps_reader = GPSReader(config.get('gps', {}))
    scanner = SignalScanner(config.get('signal', {}))
    logging.info('GPS mode: %s', gps_reader.mode)
    logging.info('Signal type: %s', scanner.mode)

    interval = config.get('logging', {}).get('interval_seconds', 5)
    mission_name = config.get('logging', {}).get('mission_name', 'rescue-mission')
    csv_path = config.get('logging', {}).get('csv_file', 'mission-data.csv')
    json_path = config.get('logging', {}).get('json_file', 'mission-data.json')

    headers = [
        'mission_name', 'timestamp', 'latitude', 'longitude', 'altitude', 'fix_type', 'satellites',
        'signal_type', 'signal_value', 'signal_details'
    ]
    write_csv_header(csv_path, headers)

    while not STOPPED:
        now = datetime.datetime.utcnow()
        gps_data = gps_reader.get_position()
        signal_data = scanner.scan()

        row = build_row(now, gps_data, signal_data, mission_name)
        append_csv(csv_path, row, headers)
        append_json(json_path, row)

        logging.info('Logged data: %s %s %s', now.isoformat(), gps_data.get('latitude'), signal_data.get('value'))
        time.sleep(interval)

    logging.info('Stopping payload logger')


if __name__ == '__main__':
    main()
