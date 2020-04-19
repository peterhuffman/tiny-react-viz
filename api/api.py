import csv
import time

# import ujson
from flask import Flask

from api.db import initialize_map_data

app = Flask(__name__)


def open_csv(file_name):
    data = []
    with open(file_name) as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]

    return data


CSV_FILENAME = "./usda_crops.csv"
SOURCE_DATA = open_csv(CSV_FILENAME)

STATE_INDEX = {'VT': 'Vermont'}
STATE_ZIP_INDEX = {'05401': 'VT'}
MAP_DATA = initialize_map_data(SOURCE_DATA)
STATE_MAP = {'VT': 'hello world'}
COUNTY_MAP = {'05401': 'Chittiden County'}


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/map-data')
def get_map_data():
    print(SOURCE_DATA[0].keys())
    response = {'map_data': MAP_DATA['2014']['CORN']}
    return {'map_data': response}
