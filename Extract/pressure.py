from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()


def get_pressure():
    pressure = sense.get_pressure()

    timestamp = datetime.utcnow().isoformat()

    return pressure
