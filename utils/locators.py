from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    LOGO = (By.ID, 'nav-logo')
    ACCOUNT = (By.ID, 'nav-link-accountList')
    SIGNUP = (By.CSS_SELECTOR, '#nav-signin-tooltip > div > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit-input')
    ERROR_MESSAGE = (By.ID, 'message_error')

class AcrisLocators(object):
    COUNTY = (By.NAME, 'select_borough')
    STREET_NUMBER = (By.NAME, 'text_street_number')
    STREET_NAME = (By.NAME, 'text_street_name')
    FIND_BBL = (By.NAME, 'submit22')
    DOCUMENT_SEARCH = (By.NAME, 'btn_docsearch')
    SEARCH = (By.NAME, 'Submit2')
    FINAL_SEARCH_OPTIONS = (By.NAME, 'Submit')

class TruePeopleLocators(object):
    REVERSE_ADDRESS_TAB = (By.ID, 'searchTypeAddress-d')
    STREET_ADDRESS_INPUT = (By.NAME, 'StreetAddress')
    CITY_STATE_ZIP_INPUT = (By.ID, 'id-d-loc-addr')
    SEARCH_BTN = (By.ID, 'btnSubmit-d-addr')
    
class NYCGovLocators(object):
    HOUSE_NUMBER_INPUT = (By.ID, 'houseno')
    STREET_NAME_INPUT = (By.ID, 'street')
    BORO_DROPDOWN = (By.ID, 'boro')
    GO_BTN = (By.CLASS_NAME, 'btn')

class GoogleMapLocators(object):
    SEARCH_BOX_INPUT = (By.ID, 'searchboxinput')
    SEARCH_BTN = (By.ID, 'searchbox-searchbutton')

class BodyLocators(object):
    BODY = (By.NAME, 'body')