import unittest
from tests.base_test import BaseTest
from pages.geodata_page import GeoDataPage


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestGeoDataPage(BaseTest):

    def test_geodata_page(self):
        print("Starting with GeoData.")
        page = GeoDataPage(self.driver)
        page.run_full_test()
        print("Finished with GeoData.")

