from dotenv import load_dotenv
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

load_dotenv()
token = os.getenv("TOKEN")

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('test_reviews_to_Google\credentials.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open_by_key('1FHCUNR7NudPSiW9Q51J178abapZSIEUlpFZwvc4lPEE')
worksheet = spreadsheet.get_worksheet(0)

url = 'https://feedbacks-api.wildberries.ru'
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(url, headers=headers)

reviews = response.json()
for review in reviews:
    worksheet.append_row([review[1],
                          review[2],
                          review[3]],)
