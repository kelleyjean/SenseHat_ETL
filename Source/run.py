import os
from multiprocessing import Pool
import Extract
from Extract.humidity import get_humidity
from Extract.temperature import get_temperature
from Extract.pressure import get_pressure

processes = ('humidity.py', 'temperature.py', 'pressure.py')


def run_process(process):
    os.system('python {}'.format(process))


pool = Pool(processes=3)
pool.map(run_process, processes)
