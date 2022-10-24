from tests.base_test import BaseTest
from pages.google_map_page import GoogleMapPage

class TestGoogleMapPage(BaseTest):

    def test_google_map_page(self):
        print("Starting with Google Maps.")
        page = GoogleMapPage(self.driver)
        page.run_full_test()
        print("Finished with Google Maps.")

