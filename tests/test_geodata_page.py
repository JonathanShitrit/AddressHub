from tests.base_test import BaseTest
from pages.geodata_page import GeoDataPage
from utils.addToCSV import add_property_to_csv

class TestGeoDataPage(BaseTest):

    def test_geodata_page(self):
        print("Adding property to addresses.csv\n")
        add_property_to_csv()

        print("Starting with GeoData.")
        page = GeoDataPage(self.driver)
        page.run_full_test()
        print("Finished with GeoData.")

