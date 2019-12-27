from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def get_humidity():
	
	humidity = sense.get_humidity()
	
	if humidity > 40:
		sense.clear(blue)
	elif humidity < 40 and humidity > 30:
		sense.clear(green)
	elif humidity < 30 and humidity > 0:
		sense.clear(red)
	sleep(1)
	
	sense.show_message(str(round(humidity,2)))
		
	print(humidity)

get_humidity()
