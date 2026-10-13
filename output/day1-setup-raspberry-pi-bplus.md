# Day 1 Setup - Raspberry Pi Model B+ (Step by Step)

## Goal for today
Bring the Raspberry Pi B+ online and ready to run the rescue payload software.

## Step 1 - Hardware readiness
Prepare these items before powering on:
- Raspberry Pi Model B+ (Rev 1.2)
- microSD card (16GB or 32GB recommended)
- 5V power supply or power bank (stable 2A recommended)
- HDMI cable + monitor (or Ethernet for headless setup)
- USB keyboard
- Ethernet cable (recommended for first setup)
- Optional: USB Wi-Fi dongle

Success check:
- All hardware is physically available and connected.

---

## Step 2 - Install OS to microSD
1. On your laptop, install Raspberry Pi Imager.
2. Choose OS: Raspberry Pi OS Lite (32-bit) for best performance on B+.
3. Choose your microSD card and write the image.
4. (Optional) In advanced settings:
   - set hostname (example: rescue-pi)
   - enable SSH
   - set username/password

Success check:
- microSD is flashed and inserted into the Pi.

---

## Step 3 - First boot and login
1. Connect power, display, keyboard, and Ethernet.
2. Boot Raspberry Pi.
3. Login using configured user account.

Success check:
- You reach the shell prompt.

---

## Step 4 - Update system packages
Run:
```bash
sudo apt update
sudo apt upgrade -y
```

Success check:
- Update and upgrade complete without critical errors.

---

## Step 5 - Install base dependencies
Run:
```bash
sudo apt install -y python3 python3-pip git gpsd gpsd-clients rtl-sdr bluez
```

Success check:
- Python, pip, gpsd, and rtl-sdr tools are installed.

---

## Step 6 - Create project folder on Pi
Run:
```bash
mkdir -p ~/rescue-payload
cd ~/rescue-payload
```

Success check:
- Folder exists and is accessible.

---

## Step 7 - Copy software to Pi
Use one method:
- Git clone from repository, or
- SCP copy from your laptop.

Example (SCP from laptop):
```bash
scp -r /path/to/location.app.rescue/payload-software/* <user>@<pi-ip>:~/rescue-payload/
```

Success check:
- Files like `main.py`, `webapp/app.py`, and `config.yaml` exist on the Pi.

---

## Step 8 - Install Python requirements
Run:
```bash
cd ~/rescue-payload
pip3 install -r requirements.txt
```

Success check:
- Dependencies install successfully.

---

## Step 9 - Quick software sanity test
Run:
```bash
python3 -m py_compile main.py gps_reader.py signal_scanner.py target_estimator.py webapp/app.py
```

Success check:
- No syntax errors.

---

## Step 10 - Run web dashboard preview
Run:
```bash
cd ~/rescue-payload/webapp
python3 app.py --port 5002
```
Open from browser on same network:
- `http://<pi-ip>:5002`

Success check:
- Dashboard loads and shows live status panel.

---

## Day 1 done when:
- Pi boots reliably
- software dependencies installed
- project files copied
- dashboard starts and is reachable in browser

## Step 2 preview (next session)
- Connect USB GPS receiver
- connect RTL-SDR or Bluetooth/Wi-Fi sensor
- verify real signal input
- start baseline scan test
