import unittest
from tests.base_test import BaseTest
from pages.true_people_search import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestTruePeopleSearchPage(BaseTest):

    # def test_page_load(self):
    #     print("Testing page loaded")
    #     page = AcrisPage(self.driver)
    #     self.assertTrue(page.check_page_loaded())

    def test_insert_property_address(self):
        print("Starting with TruePeople.")
        page = TruePeopleSearchPage(self.driver)
        page.run_full_test()
        print("Finished with TruePeople.")

# TODO: Figure out a way to loop through the tests and open new tabs for each new test

