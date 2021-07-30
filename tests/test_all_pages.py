import unittest
from tests.base_test import BaseTest
from pages.acris_page import AcrisPage
from pages.true_people_search import TruePeopleSearchPage
from pages.nyc_gov_page import NYCGovPage
from pages.google_map_page import GoogleMapPage
from pages.geodata_page import GeoDataPage


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestAllPages(BaseTest):

    def test_all_pages(self):
        print("Starting with Acris.")
        acris_page = AcrisPage(self.driver)
        acris_page.run_full_test()
        print("Finished with Acris.\n")

        print("Starting with TruePeople.")
        true_people = TruePeopleSearchPage(self.driver)
        true_people.run_full_test()
        print("Finished with True People.\n")

        print("Starting with NYC Gov.")
        nyc_gov_page = NYCGovPage(self.driver)
        nyc_gov_page.run_full_test()
        print("Finished with NYC Gov.\n")

        print("Starting with Google Maps.")
        google_map_page = GoogleMapPage(self.driver)
        google_map_page.run_full_test()
        print("Finished with Google Maps.\n")

        print("Starting with GeoData.")
        geodata_page = GeoDataPage(self.driver)
        geodata_page.run_full_test()
        print("Finished with GeoData.")

