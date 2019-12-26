from sense_hat import SenseHat

sense = SenseHat()


def get_pressure():
	
	pressure = sense.get_pressure()
	
	return pressure
