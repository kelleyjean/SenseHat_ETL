from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import csv
import time

sense = SenseHat()

filepath = '/home/pi/Desktop/SenseHat_ETL/DataFiles/'

def get_pressure():
    pressure_list = []
    pressure = sense.get_pressure()
    timestamp = datetime.utcnow().isoformat()
    pressure_list.append(pressure)
    pressure_list.append(timestamp)
    return pressure_list

try:
    
    with open(filepath + 'pressure_data.csv', 'w') as file:
        data_writer = writer(file)

        while True:
            data = get_pressure()
            data_writer.writerow(data)
            time.sleep(30)
        
except KeyboardInterrupt:
	print('Pressure Done.')
