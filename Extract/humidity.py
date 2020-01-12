from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()


def get_humidity():
    humidity = sense.get_humidity()

    timestamp = datetime.utcnow().isoformat()

    return humidity
