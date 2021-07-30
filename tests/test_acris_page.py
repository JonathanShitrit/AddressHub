import unittest
from tests.base_test import BaseTest
from pages.acris_page import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestAcrisPage(BaseTest):

    # def test_page_load(self):
    #     print("Testing page loaded")
    #     page = AcrisPage(self.driver)
    #     self.assertTrue(page.check_page_loaded())

    def test_inserting_property_address(self):
        print("Starting with Acris.")
        page = AcrisPage(self.driver)
        # page.insert_property_address()
        # page.click_find_bbl()
        # page.click_doc_search()
        # page.click_search()
        # page.find_search_options()
        page.run_full_test()
        print("Finished with Acris.")
