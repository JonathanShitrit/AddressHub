import unittest
from tests.base_test import BaseTest
from pages.google_map_page import GoogleMapPage


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestGoogleMapPage(BaseTest):

    def test_google_map_page(self):
        print("Starting with Google Maps.")
        page = GoogleMapPage(self.driver)
        page.run_full_test()
        print("Finished with Google Maps.")

