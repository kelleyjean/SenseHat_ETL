from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()


def get_temperature():

	temp_c = sense.get_temperature()
	temp_f = ((temp_c/5) * 9) + 32

	timestamp = datetime.utcnow().isoformat()

	return temp_c, temp_f

