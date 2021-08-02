from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from utils.locators import BodyLocators

tab_index = 0
# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        if self.wait_element(*locator):
            return self.driver.find_element(*locator)
        return None
        
    def new_tab(self):
        global tab_index

        # If this is the first page, open page in current (first) tab
        if tab_index == 0:
            self.driver.get(self.base_url)
            tab_index += 1
            return 

        # Else, open a new tab and switch to it
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[tab_index])
        self.driver.get(self.base_url)
        tab_index += 1     

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            return False
            # self.driver.quit()

  
    # def get_element(self, *locator, wait=10):
    #     self.wait_to_appear(wait)
    #     return self.driver.find_element(*locator)

    # def get_all_elements(self, wait=10):
    #     self.wait_to_appear(wait)
    #     return self.driver.find_elements(*locator)

    # # def get_locator(self):
    # #     return self.locator

    # def get_text(self, encoding=None):
    #     text = self.get_element().text
    #     return text.encoding(encoding) if encoding else text

    # def get_attribute(self, value):
    #     return self.get_element().get_attribute(value)
        
    # def is_selected(self, value):
    #     return self.get_element().is_selected()

    # def is_checked(self, value):
    #     return self.driver.execute_script("return arguments[0].checked;", slef.get_element())

    # def exists(self, *locator):
    #     try:
    #         WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(*locator))
    #         return True
    #     except:
    #         return False
    
    # def is_clickable(self):

    #     def is_clickable(by, locator):
    #         try:
    #             WebDriverWait(Browser.get_driver(), 1).until(EC.presence_of_element_located((by, locator)))
    #             return True
    #         except:
    #             return False
        
    #     return self.exists() and is_clickable(self.by, self.locator)

    # def wait_to_be_clickable(self, seconds=10, ignore_error=False):
    #     start = time.time()
    #     while (time.time() - start) < seconds:
    #         if self.is_clickable():
    #             return self
    #         time.sleep(1)
    #     if not ignore_error:
    #         if self.exists():
    #             return AssertionError("Locator in the DOM: {} but did not become clickable in {} seconds"
    #                                     .format(self.locator, seconds))
    #         raise AssertionError("Locator is not in the DOM and so not clickable: {}".format(self.locator))
    #     else:
    #         return self

    # def wait_to_appear(self, seconds=10, ignore_error=False):
    #     start = time.time()
    #     while (time.time() - start) < seconds:
    #         if self.is_clickable():
    #             return self
    #     if not ignore_error:
    #         raise AssertionError("Locator: {} did not appear in {} seconds!".format(self.locator, seconds))
    #     else:
    #         return self

    # def click(self, wait=10, use_action_chain=False):
    #     self.wait_to_be_clickable(wait)
    #     initial_handles = Browser.get_driver().window_handles

    #     if use_action_chain:
    #         ui_object = self.get_element()
    #         ActionChains(Browser.get_driver()).move_to_element(ui_object).click().perform()
    #     else:
    #         try:
    #             self.get_element().click()
    #         except Exception as error:
    #             if "Other element would receive the click" in error.message:
    #                 self.scrollIntoCenter()
    #                 self.get_element().click()
    #             else:
    #                 raise error

    #     if len(Browser.get_driver().window_handles) > len(initial_handles):
    #         Browser.switch_to_latest_active_window()
    #     return self


    # def set_text(self, value, loose_focus=False):
    #     self.get_element().clear()
    #     self.get_element().send_keys(str(value))
    #     if loose_focus:
    #         self.press_key(Keys.TAB)
    #     return self

    # def type_text(self, value):
    #     self.get_element().send_keys(value)
    #     return self

    # def press_key(self, key, use_action_chain=False):
    #     if not use_action_chain:
    #         self.get_element().send_keys(Key)
    #     else:
    #         chains = ActionChains(driver=Browser.get_driver())
    #         chains.send_keys(Key).perform()
    #     return self

    # def mouse_over(self):
    #     ui_object = self.get_element()
    #     ActionChains(Browser.get_driver()).move_to_element(ui_object).perform()
    #     return self