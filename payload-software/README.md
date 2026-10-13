# Raspberry Pi Payload Software

## Purpose
This software is designed to run on a Raspberry Pi payload attached to a drone. It logs GPS position and signal sensor readings during each mission and provides a simple operator dashboard.

## Files
- `main.py` - entrypoint for the payload program
- `config.yaml` - sample configuration for GPS, sensor, and logging
- `requirements.txt` - Python dependencies
- `gps_reader.py` - helper for GPS data
- `signal_scanner.py` - helper for signal scanning
- `target_estimator.py` - simple target estimation model for weak-signal rescue detection
- `webapp/app.py` - Flask web dashboard
- `webapp/templates/index.html` - operator-facing interface

## Install
1. Flash Raspberry Pi OS to the MicroSD card.
2. Boot the Pi and install dependencies:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip gpsd gpsd-clients rtl-sdr bluez -y
   pip3 install -r requirements.txt
   ```

## Configure
1. Edit `config.yaml` to match your hardware.
2. Set the correct `csv_file` and `json_file` paths.
3. Choose the sensor type:
   - `bluetooth` for BLE/Wi-Fi beacon scanning
   - `wifi` for Wi-Fi network scans
   - `rtl_sdr` for radio frequency scanning
   - `simulated` for testing without hardware
4. Optional target estimation settings can be added under `target_estimation` in the config.

## Run
```bash
python3 main.py --config config.yaml
```

## Web dashboard
Start the web interface for the operator:
```bash
cd webapp
python3 app.py --port 5000
```
Open the dashboard in a browser at `http://<pi-ip>:5000`.

## Prototype behavior
The dashboard now supports:
- a signal detection view
- an estimated target label
- estimated distance in meters
- a confidence percentage
- a mode switch for:
  - `both`
  - `rescue` for weak-signal rescue-style detection
  - `normal` for nearby-signal detection

## Notes
- Use the `simulated` sensor type for the first test flight.
- Make sure GPS is connected and `gpsd` is running if using `gpsd` mode.
- Logs are written as CSV and JSON to the configured output paths.
