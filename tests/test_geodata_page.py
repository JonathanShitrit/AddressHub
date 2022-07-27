from tests.base_test import BaseTest
from pages.geodata_page import GeoDataPage

class TestGeoDataPage(BaseTest):

    def test_geodata_page(self):
        print("Starting with GeoData.")
        page = GeoDataPage(self.driver)
        page.run_full_test()
        print("Finished with GeoData.")

