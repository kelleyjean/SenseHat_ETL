from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import csv
import time

sense = SenseHat()


def get_pressure():
    pressure_list = []
    pressure = sense.get_pressure()
    timestamp = datetime.utcnow().isoformat()
    pressure_list.append(pressure)
    pressure_list.append(timestamp)
    return pressure_list

with open('pressure_data.csv', 'w') as file:
    data_writer = writer(file)

    while True:
        data = get_humidity()
        data_writer.writerow(data)
        time.sleep(5)
