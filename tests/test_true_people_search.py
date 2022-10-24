from tests.base_test import BaseTest
from pages.true_people_search import *
from utils.addToCSV import add_property_to_csv

class TestTruePeopleSearchPage(BaseTest):

    def test_insert_property_address(self):
        print("Adding property to addresses.csv\n")
        add_property_to_csv()
        
        print("Starting with TruePeople.")
        page = TruePeopleSearchPage(self.driver)
        page.run_full_test()
        print("Finished with TruePeople.")

