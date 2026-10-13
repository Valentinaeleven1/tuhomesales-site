# Drone Payload Field Reference

## Purpose
A quick reference handout for the Raspberry Pi drone payload kit and mission launch workflow.

## Payload kit contents
- Raspberry Pi 4 Model B (4GB) or Raspberry Pi Zero 2 W
- Raspberry Pi power supply or 5V USB power bank
- USB GPS receiver
- Signal sensor module:
  - RTL-SDR dongle for radio scanning, or
  - USB Bluetooth/Wi-Fi adapter for beacon detection
- MicroSD card (32GB or larger) with Raspberry Pi OS and rescue software
- Compact case or enclosure
- Lightweight mount, straps, or bracket for drone attachment
- Cable ties and padding for secure mounting

## Optional items
- Small USB hub (if more than one USB device is needed)
- External antenna for the signal receiver if needed
- Portable charger or spare batteries
- Weather protection enclosure for dust or light moisture

## Mounting checklist
- Attach the payload securely to the drone.
- Keep the weight centered and balanced.
- Use straps, mounts, or brackets designed for the drone.
- Secure cabling and protect against vibration.
- Confirm payload weight stays under drone limits.

## Startup checklist
1. Connect the power bank to the Raspberry Pi.
2. Power on the Raspberry Pi.
3. Wait for full boot.
4. Start the rescue program using the provided command.
5. Confirm GPS and sensor data are recording.

## Mission checklist
- Ensure the drone has GPS lock.
- Verify the drone is ready for flight.
- Start the mission from the drone controller.
- Monitor payload status if possible.
- Keep the flight path safe and clear.

## Post-mission checklist
- Land the drone safely.
- Power down the Raspberry Pi.
- Remove the payload and check components.
- Retrieve log files from the Raspberry Pi.
- Upload or deliver the data for analysis.

## Important notes
- You are capturing a signal pattern, not decoding a phone call.
- The goal is to detect a phone-related/emergency signal, not raw cellular content.
- Use a test flight first to confirm the full workflow.
- Prioritize safety and clear communication with the drone operator.
