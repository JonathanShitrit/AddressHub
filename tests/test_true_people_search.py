from tests.base_test import BaseTest
from pages.true_people_search import *

class TestTruePeopleSearchPage(BaseTest):

    def test_insert_property_address(self):
        print("Starting with TruePeople.")
        page = TruePeopleSearchPage(self.driver)
        page.run_full_test()
        print("Finished with TruePeople.")

