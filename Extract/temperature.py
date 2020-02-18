from sense_hat import SenseHat
from datetime import datetime
import csv
from csv import writer
import time

sense = SenseHat()

filepath = '/home/pi/Desktop/SenseHat_ETL/DataFiles/'

def get_temperature():
	temp_list = []
	temp_c = sense.get_temperature()
	temp_f = ((temp_c/5) * 9) + 32
	timestamp = datetime.utcnow().isoformat()
	temp_list.append(temp_c)
	temp_list.append(temp_f)
	temp_list.append(timestamp)
	return temp_list

try: 
	
	with open(filepath + 'temperature_data.csv', 'w') as file:
		data_writer = writer(file)

		while True:
			data = get_temperature()
			data_writer.writerow(data)
			time.sleep(30)
        
except KeyboardInterrupt:
	print('Temperature Done.')
