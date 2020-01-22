import os
from multiprocessing import Pool


filepath = ('/home/pi/Desktop/SenseHat_ETL/Extract/')

processes = (filepath + 'humidity.py', filepath + 'temperature.py', filepath + 'pressure.py')


def run_process(process):
    os.system('python {}'.format(process))


pool = Pool(processes=3)
pool.map(run_process, processes)
