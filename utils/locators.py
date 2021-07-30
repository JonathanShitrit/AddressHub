from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

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

class GeoDataLocators(object):
    # "loginRegisterErrorMobile"
    # /html/body/div[1]/div[2]/header[1]/div/div/div/nav/div/div[2]/div[1]/ul/li/ul/li[1]/div/div/a
    # "loginRegisterErrorMobile"
    # /html/body/div[1]/div[2]/header[2]/div/div[2]/div/nav/div/div[3]/div[1]/ul[2]/li/ul/li[1]/div/div/a
    # "loginRegisterError"
    # /html/body/div[1]/div[2]/header[2]/div/div[2]/div/nav/div/div[3]/div[2]/ul/li[10]/div/a

    LOGIN_MODAL = (By.XPATH, '/html/body/div[1]/div[2]/header[2]/div/div[2]/div/nav/div/div[3]/div[2]/ul/li[10]/div/a')
    LOGIN_EMAIL_INPUT = (By.ID, 'LoginModal_Email')
    LOGIN_PASSWORD_INPUT = (By.ID, 'LoginModal_Password')
    LOGIN_SUBMIT_BTN = (By.ID, 'LoginModal_Submit')

class BodyLocators(object):
    BODY = (By.NAME, 'body')  