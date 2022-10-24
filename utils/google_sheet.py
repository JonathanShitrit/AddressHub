import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheet():
    def __init__(self) -> None:
        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/spreadsheets']
        # use creds to create a client to interact with the Google Drive API
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/shitritj/Documents/AddressHub/utils/addresshub-366516-1ffd3a7faac0.json', self.scope)
        self.client = gspread.authorize(self.creds)
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        self.sheet = self.client.open("addresses").sheet1

    def add_address_to_sheet(self, address):
        print("Adding property to Google Sheet...")
        self.sheet.append_row(address)
        print("Successfully added.")