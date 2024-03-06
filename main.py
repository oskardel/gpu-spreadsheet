import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(credentials=credentials)

sheet_id = "1NSfKKmZMTfxyObacflA8OfjBPA66OrSuyfi_Ox0v1Go"
sheet = client.open_by_key(key=sheet_id)
