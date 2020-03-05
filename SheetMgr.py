import json
import sys
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

oauth_key_file = 'googleapi-token.json' 
gss_scopes =  ['https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive']
spreadsheet_key = "1pGn-4H6gzWrZVvP7gOitmgcP8pVPPSyvD6r2kMnPu-E"
spreadsheet_name = "vocabulary"

credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, gss_scopes)
gc = gspread.authorize(credentials)
worksheet = gc.open_by_key(spreadsheet_key).sheet1



def search_word(word,language ):
    global worksheet
    try :
        cell = worksheet.find(word)
        row = cell.row
        col = cell.cel
        if(language =="chinese") :
            return worksheet.cell(row, col-1).value
        else :
            return worksheet.cell(row, col+1).value
    except  gspread.exceptions as gs :
        return "查無此字"
        raise gs

def add_word (voc ,chi) :
    global worksheet
    res = search_word(voc)
    
    if(res == "查無此字") :
        vlist = worksheet.row_values(1)
        last_row = vlist.len()+1
        worksheet.update_cell(last_row, 1, voc)
        worksheet.update_cell(last_row, 2, chi)
        return True
    else :
        return False
    
        
    
        



    

    



