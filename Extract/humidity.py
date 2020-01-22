from sense_hat import SenseHat
from datetime import datetime
import csv
from csv import writer

sense = SenseHat()


def get_humidity():
    humidity_list = []
    humidity = sense.get_humidity()
    timestamp = datetime.utcnow().isoformat()
    humidity_list.append(humidity)
    humidity_list.append(timestamp)
    return humidity_list


with open('humidity_data.csv', 'w') as file:
    data_writer = writer(file)

    while True:
        data = get_humidity()
        data_writer.writerow(data)
