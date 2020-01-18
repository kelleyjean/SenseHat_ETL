from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()


def get_humidity():
    humidity_list = []
    humidity = sense.get_humidity()
    timestamp = datetime.utcnow().isoformat()
    humidity_list.append(humidity)
    humidity_list.append(timestamp)
    return humidity_list
