import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>
class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1080,1080")
        # options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        global d
        d = webdriver.Chrome(options=options)
        self.driver = d
        # self.driver = webdriver.Chrome(options=options)
        
        print("Starting up!")

    # def tearDown(self):
    #     print(999)
    #     self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)
