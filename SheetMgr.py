import json
import sys
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

oauth_key_file = 'googleapi-token.json' 
scope =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
spreadsheet_path = "1pGn-4H6gzWrZVvP7gOitmgcP8pVPPSyvD6r2kMnPu-E"





def addvoc(voc,chi) :
    try:
        # Login if necessary.
        worksheet = login_open_sheet(oauth_key_file, spreadsheet_path)
        # Append the data in the spreadsheet
        worksheet.append_row(voc , chi) #將資料加在最下方
        print ("add successful")
        return True
    except:
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Error, logging in again')
        return False
       
        

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        
        worksheet = gc.open(spreadsheet_path).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)
        



    

    



