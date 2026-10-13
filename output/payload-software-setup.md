# Raspberry Pi Payload Software Setup

## Overview
This guide describes how to prepare the Raspberry Pi payload for drone-assisted signal search. It covers OS setup, software installation, and program loading.

## Step 1: Prepare the Raspberry Pi
1. Download Raspberry Pi OS Lite from the official website.
2. Use Raspberry Pi Imager or Balena Etcher to write the OS image to the MicroSD card.
3. Enable SSH if needed by creating an empty file named `ssh` in the boot partition.
4. Insert the MicroSD card into the Raspberry Pi.

## Step 2: Boot and configure the Pi
1. Connect the Raspberry Pi to a monitor, keyboard, or use SSH.
2. Power it on and complete the initial setup.
3. Update the system:
   - `sudo apt update`
   - `sudo apt upgrade -y`
4. Install required packages:
   - `sudo apt install python3 python3-pip git -y`

## Step 3: Install GPS and sensor support
1. Plug in the USB GPS receiver.
2. Plug in the signal sensor module (RTL-SDR dongle or Bluetooth/Wi-Fi adapter).
3. Install RTL-SDR tools if using RTL-SDR:
   - `sudo apt install rtl-sdr -y`
4. Install Python libraries for GPS and signal processing:
   - `pip3 install pyserial gpsd-py3 numpy requests`

## Step 4: Load your rescue program
1. Copy your program repository to the Raspberry Pi using `git clone` or file transfer.
2. Place the software in a dedicated folder, for example `/home/pi/rescue-payload`.
3. Install any Python dependencies from `requirements.txt` if present:
   - `pip3 install -r requirements.txt`

## Step 5: Configure logging and output
1. Create a configuration file for the program with:
   - GPS device path
   - signal sensor settings
   - data logging path
2. Ensure the program logs data locally in a format that can be uploaded later.
3. Example log location: `/home/pi/rescue-payload/logs/mission-data.csv`

## Step 6: Test the payload software
1. Run the program on the ground first.
2. Verify GPS position is captured.
3. Verify signal sensor data is recorded when the expected signal is present.
4. Confirm the program writes timestamped location and signal readings.

## Step 7: Finalize the kit
1. Power down the Raspberry Pi.
2. Pack the Pi, sensor, GPS, power bank, and cables together.
3. Include a short note with startup instructions:
   - connect power
   - wait for boot
   - start the program
4. Send the full payload kit to the drone operator.

## Optional: Remote upload support
- If the payload can connect to the internet, include support for uploading logs to the backend.
- Otherwise, plan to retrieve the data manually after the mission.
