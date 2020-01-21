from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()


def get_temperature():
	temp_list = []
	temp_c = sense.get_temperature()
	temp_f = ((temp_c/5) * 9) + 32
	timestamp = datetime.utcnow().isoformat()
	temp_list.append(temp_c)
	temp_list.append(temp_f)
	temp_list.append(timestamp)
	return temp_list

