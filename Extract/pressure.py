from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()


def get_pressure():
    pressure_list = []
    pressure = sense.get_pressure()
    timestamp = datetime.utcnow().isoformat()
    pressure_list.append(pressure)
    pressure_list.append(timestamp)
    return pressure_list
