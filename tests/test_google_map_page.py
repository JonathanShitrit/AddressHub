from tests.base_test import BaseTest
from pages.google_map_page import GoogleMapPage
from utils.addToCSV import add_property_to_csv

class TestGoogleMapPage(BaseTest):

    def test_google_map_page(self):
        print("Adding property to addresses.csv\n")
        add_property_to_csv()
        
        print("Starting with Google Maps.")
        page = GoogleMapPage(self.driver)
        page.run_full_test()
        print("Finished with Google Maps.")

