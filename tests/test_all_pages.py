from tests.base_test import BaseTest
from pages.acris_page import AcrisPage
from pages.true_people_search import TruePeopleSearchPage
from pages.nyc_gov_page import NYCGovPage
from pages.google_map_page import GoogleMapPage
from pages.geodata_page import GeoDataPage

class TestAllPages(BaseTest):

    def test_all_pages(self):
        try:
            print("Opening Acris.")
            acris_page = AcrisPage(self.driver)
            acris_page.run_full_test()
            print("Finished with Acris.\n")
        except Exception as e:
            print("\nSomething failed with Acris.", e,"\n")

        try:
            print("Opening TruePeople.")
            true_people = TruePeopleSearchPage(self.driver)
            true_people.run_empty_test()
            print("Finished with True People.\n")
        except Exception as e:
            print("\nSomething failed with TruePeople.", e,"\n")

        try:        
            print("Opening Google Maps.")
            google_map_page = GoogleMapPage(self.driver)
            google_map_page.run_empty_test()
            print("Finished with Google Maps.\n")
        except Exception as e:
            print("\nSomething failed with Google Maps.", e,"\n")

        try:        
            print("Opening GeoData.")
            geodata_page = GeoDataPage(self.driver)
            geodata_page.run_full_test()
            print("Finished with GeoData.\n")
        except Exception as e:
            print("\nSomething failed with GeoData.", e,"\n")

        try:
            print("Opening NYC Gov.")
            nyc_gov_page = NYCGovPage(self.driver)
            nyc_gov_page.run_empty_test()
            print("Finished with NYC Gov.\n")
        except Exception as e:
            print("\nSomething failed with NYC Gov.", e,"\n")
