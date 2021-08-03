# AddressHub

Address hub is a web automation tool which inserts property addresses into 5 different websites for you. This way you can get to the property details quicker. This project utilizes the Page-object-model (POM) pattern. This Design Pattern is used in Selenium where web pages are represented by a corresponding class and web elements are represented by the variables of the class and all interactions are possible through the methods or say functions of the class.

## Advantages of POM model:

* Reusability: We can inherit from the base_page class in different test cases which means the code for identifying web elements and methods to interact with them can easily be reused.
* Code separation – Keep test and locators separately, makes our code clean, easy to understand, and maintain
* Maintainability: Test case and page class are different from each other which means we can easily update the code if the user interface changes. The fix needs changes in only one place.
* Readability: New team members can easily start writing tests by following the existing structure.

### Get Started
1. clone this repo
2. Make sure you have python3 and pip installed on your machine
3. Navigate into the folder and run these 3 commands
```sh
pip install selenium
pip install python-dotenv
pip install webdriver-manager
```
4. Save an .env file to the project with the property address you want to automate. ex:
```sh
STREET_NUMBER=123
STREET_NAME=main
SUFFIX=st
COUNTY=queens
CITY=flushing
STATE=ny
EMAIL=INSERT_EMAIL_FOR_GEODATADIRECT
PASSWORD=INSERT_PASSWORD_FOR_GEODATADIRECT
```
5. You can now run the tests below

#### If you want to run all tests, you should type: 
```sh
 python -m unittest tests.test_all_pages 
```

#### If you want to run one specific website, you should type: 
```sh
python -m unittest tests.test_nyc_gov_page
```
