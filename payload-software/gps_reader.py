import logging

try:
    from gps import gps, WATCH_ENABLE, WATCH_NEWSTYLE
    GPSD_AVAILABLE = True
except ImportError:
    GPSD_AVAILABLE = False

try:
    import serial
    SERIAL_AVAILABLE = True
except ImportError:
    SERIAL_AVAILABLE = False


def parse_nmea_sentence(sentence):
    parts = sentence.strip().split(',')
    if parts[0] == '$GPGGA' and len(parts) > 9:
        try:
            lat = float(parts[2])
            lat_dir = parts[3]
            lon = float(parts[4])
            lon_dir = parts[5]
            altitude = float(parts[9])
            return {
                'latitude': convert_nmea_position(lat, lat_dir),
                'longitude': convert_nmea_position(lon, lon_dir),
                'altitude': altitude,
                'fix_type': 'GPGGA',
                'satellites': None
            }
        except Exception:
            return None
    return None


def convert_nmea_position(value, direction):
    degrees = int(value / 100)
    minutes = value - (degrees * 100)
    pos = degrees + minutes / 60.0
    if direction in ['S', 'W']:
        pos = -pos
    return pos


class GPSReader:
    def __init__(self, config):
        self.mode = config.get('type', 'gpsd')
        self.config = config
        if self.mode == 'gpsd' and GPSD_AVAILABLE:
            self.session = gps(host=config.get('host', 'localhost'), port=config.get('port', 2947))
            self.session.stream(WATCH_ENABLE | WATCH_NEWSTYLE)
        else:
            self.session = None
            self.serial_port = config.get('serial_port')
            self.baudrate = config.get('baudrate', 9600)

    def get_position(self):
        if self.mode == 'gpsd' and self.session:
            return self._read_gpsd()
        elif self.mode == 'serial' and SERIAL_AVAILABLE and self.serial_port:
            return self._read_serial()
        else:
            return self._simulated_position()

    def _read_gpsd(self):
        try:
            report = self.session.next()
            if report['class'] == 'TPV':
                return {
                    'latitude': getattr(report, 'lat', None),
                    'longitude': getattr(report, 'lon', None),
                    'altitude': getattr(report, 'alt', None),
                    'fix_type': getattr(report, 'mode', None),
                    'satellites': getattr(report, 'satellites', None)
                }
        except Exception as exc:
            logging.warning('GPSD read failed: %s', exc)
        return self._simulated_position()

    def _read_serial(self):
        try:
            ser = serial.Serial(self.serial_port, self.baudrate, timeout=2)
            line = ser.readline().decode('ascii', errors='ignore')
            ser.close()
            parsed = parse_nmea_sentence(line)
            if parsed:
                return parsed
        except Exception as exc:
            logging.warning('Serial GPS read failed: %s', exc)
        return self._simulated_position()

    def _simulated_position(self):
        logging.warning('Using simulated GPS position')
        return {
            'latitude': None,
            'longitude': None,
            'altitude': None,
            'fix_type': 'none',
            'satellites': None
        }
