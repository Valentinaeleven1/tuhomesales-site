import logging
import random
import subprocess

try:
    from rtlsdr import RtlSdr
    RtlSdrAvailable = True
except ImportError:
    RtlSdrAvailable = False


class SignalScanner:
    def __init__(self, config):
        self.mode = config.get('type', 'simulated')
        self.duration = config.get('scan_duration', 5)
        self.interface = config.get('interface', 'hci0')
        self.frequency_mhz = config.get('frequency_mhz', 915.0)
        self.rtlsdr = config.get('rtl_sdr', {})

    def scan(self):
        if self.mode == 'rtl_sdr':
            return self._scan_rtl_sdr()
        if self.mode == 'bluetooth':
            return self._scan_bluetooth()
        if self.mode == 'wifi':
            return self._scan_wifi()
        return self._simulated_scan()

    def _scan_rtl_sdr(self):
        if not RtlSdrAvailable:
            logging.warning('RTL-SDR library unavailable, using simulated result')
            return self._simulated_scan()
        try:
            with RtlSdr() as s:
                s.sample_rate = float(self.rtlsdr.get('sample_rate', 2.4e6))
                s.center_freq = float(self.frequency_mhz) * 1e6
                s.gain = self.rtlsdr.get('gain', 'auto')
                samples = s.read_samples(int(self.rtlsdr.get('num_samples', 256000)))
                power = 20 * np.log10((abs(samples).mean() + 1e-8))
                return {
                    'type': 'rtl_sdr',
                    'value': round(power, 2),
                    'details': f'center_freq={self.frequency_mhz} MHz'
                }
        except Exception as exc:
            logging.warning('RTL-SDR scan failed: %s', exc)
            return self._simulated_scan()

    def _scan_bluetooth(self):
        try:
            result = subprocess.run(
                ['timeout', str(self.duration), 'hcitool', 'lescan', '--duplicates'],
                capture_output=True,
                text=True,
                check=False
            )
            if result.stdout:
                lines = [line for line in result.stdout.splitlines() if line.strip()]
                count = len(lines)
                return {
                    'type': 'bluetooth',
                    'value': count,
                    'details': f'{count} BLE advertisements seen'
                }
        except Exception as exc:
            logging.warning('Bluetooth scan failed: %s', exc)
        return self._simulated_scan()

    def _scan_wifi(self):
        try:
            result = subprocess.run(
                ['nmcli', '-f', 'BSSID,SSID,SIGNAL', 'dev', 'wifi', 'list'],
                capture_output=True,
                text=True,
                check=False
            )
            if result.stdout:
                lines = [line for line in result.stdout.splitlines() if line.strip() and not line.startswith('BSSID')]
                count = len(lines)
                return {
                    'type': 'wifi',
                    'value': count,
                    'details': f'{count} Wi-Fi networks detected'
                }
        except Exception as exc:
            logging.warning('Wi-Fi scan failed: %s', exc)
        return self._simulated_scan()

    def _simulated_scan(self):
        value = random.randint(0, 5)
        return {
            'type': 'simulated',
            'value': value,
            'details': 'simulated sensor output'
        }
