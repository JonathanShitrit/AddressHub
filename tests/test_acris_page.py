from tests.base_test import BaseTest
from pages.acris_page import *

class TestAcrisPage(BaseTest):

    def test_inserting_property_address(self):
        print("Starting with Acris.")
        page = AcrisPage(self.driver)
        page.run_full_test()
        print("Finished with Acris.")
