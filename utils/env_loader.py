from dotenv import load_dotenv
import os

load_dotenv()

STREET_NUMBER = os.getenv("STREET_NUMBER")
STREET_NAME = os.getenv("STREET_NAME")
UNIT = os.getenv("UNIT")
COUNTY = os.getenv("COUNTY")
CITY = os.getenv("CITY")
STATE = os.getenv("STATE")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def get_boro_id():
    boro_ids = {"manhattan": "1", "bronx": "2", "brooklyn": "3", "queens": "4", "staten island": "5"}
    return boro_ids.get(COUNTY.lower())