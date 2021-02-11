import gspread
from google.oauth2.service_account import Credentials
import config

class Sheet:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets',
                       'https://www.googleapis.com/auth/drive']
        self.credentials = Credentials.from_service_account_file(
            'cerdentialFile.json',
            scopes=self.scopes
        )
        self.gc = gspread.authorize(self.credentials)
        self.sh = self.gc.open_by_key(config.GOOGLE_SHEET_ID)
        self.ws = self.sh.worksheet(config.GOOGLE_WORK_SHEET)

    def get_line(self):
        """
        This function is needed to get a new line for sequential writing
        """
        return len(self.sh.values_get('A1:A1000')['values']) + 1

    def set_value(self, range: str, params: list):
        """
        This function is required to write to the table
        """
        self.ws.update(range, params)

    def get_value(self, range: str):
        """
        This function is needed to get data from a cell in a table
        """
        return self.ws.acell(range).value

    def get_values_column(self, column: int):
        """
        This function is needed to get data from a column in a table
        """
        return self.ws.col_values(column)
    
    def get_values_row(self, row: int):
        """
        This function is needed to get data from a row in a table
        """
        return self.ws.row_values(row)
