import gspread
from google.oauth2.service_account import Credentials
import config

class Sheet:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets',
                       'https://www.googleapis.com/auth/drive']
        self.credentials = Credentials.from_service_account_file(
            'pybottestsheet-15c43cb159da.json',
            scopes=self.scopes
        )
        self.gc = gspread.authorize(self.credentials)
        self.sh = self.gc.open_by_key(config.GOOGLE_SHEET_ID)
        self.ws = self.sh.worksheet(config.GOOGLE_WORK_SHEET)

    def get_line(self):
        return len(self.sh.values_get('A1:A1000')['values']) + 1

    def set_value(self, range: str, params: list):
        self.ws.update(range, params)

    def get_value(self, range: str):
        return self.ws.acell(range).value

    def get_values(self, column: int):
        return self.ws.col_values(column)
