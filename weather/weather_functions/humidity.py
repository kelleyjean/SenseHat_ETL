from sense_hat import SenseHat

sense = SenseHat()

def get_humidity():
	
	humidity = sense.get_humidity()
	
	return humidity
