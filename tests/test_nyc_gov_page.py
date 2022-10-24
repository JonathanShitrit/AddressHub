from tests.base_test import BaseTest
from pages.nyc_gov_page import NYCGovPage
from utils.addToCSV import add_property_to_csv

class TestNYCGovPage(BaseTest):

    def test_nyc_gov_page(self):
        print("Adding property to addresses.csv\n")
        add_property_to_csv()
        
        print("Starting with NYC Gov.")
        page = NYCGovPage(self.driver)
        page.run_full_test()
        print("Finished with NYC Gov.")

