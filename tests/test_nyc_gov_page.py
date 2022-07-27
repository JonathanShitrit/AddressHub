from tests.base_test import BaseTest
from pages.nyc_gov_page import NYCGovPage

class TestNYCGovPage(BaseTest):

    def test_nyc_gov_page(self):
        print("Starting with NYC Gov.")
        page = NYCGovPage(self.driver)
        page.run_full_test()
        print("Finished with NYC Gov.")

