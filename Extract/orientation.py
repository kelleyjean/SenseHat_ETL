from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

def get_sense_data():
	sense_data = []
	orientation = sense.get_orientation()
	sense_data.append(orientation["yaw"])
	sense_data.append(orientation["pitch"])
	sense_data.append(orientation["roll"])

	return sense_data

while True:
	print(get_sense_data())
