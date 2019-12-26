from sense_hat import SenseHat

sense = SenseHat()


def get_temperature():

	temp = sense.get_temperature()
	temp = ((temp/5) * 9) + 32
	
	return temp
