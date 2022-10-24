import csv
import os
from re import I
from utils.env_loader import *

def add_property_to_csv():
    output_file = f'addresses.csv'
    write_mode = 'w'

    file_exists = os.path.exists(os.path.join('output', output_file))
    if file_exists:
        write_mode = 'a'

    with open(os.path.join('output', output_file), write_mode) as f:
        writer = csv.writer(f)

        if file_exists == False:
            header = ["STREET_NUMBER", "STREET_NAME", "SUFFIX", "CITY", "COUNTY", "STATE"]
            writer.writerow(header)


        property = [STREET_NUMBER, STREET_NAME, SUFFIX, CITY, COUNTY, STATE]
        writer.writerow(property)

    return output_file