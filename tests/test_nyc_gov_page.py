import unittest
from tests.base_test import BaseTest
from pages.nyc_gov_page import NYCGovPage


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestNYCGovPage(BaseTest):

    def test_nyc_gov_page(self):
        print("Starting with NYC Gov.")
        page = NYCGovPage(self.driver)
        page.run_full_test()
        print("Finished with NYC Gov.")

