import sys
import gspread
import random
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
        col = cell.col
        if(language =="english") :
            print( worksheet.row_values(row)[1:])
            return worksheet.row_values(row)[1:]
        else :
            return worksheet.cell(row, 1).value
    except  gspread.exceptions.CellNotFound as gs :
        print ("no result")
        return "no result"
        raise gs

def add_word (voc ,chi) :
    global worksheet
    voc = voc.strip()
    res = search_word(voc,"english")
    
    if(res == "no result") :
        vlist = worksheet.get_all_values()
        last_row = len(vlist)+1
        print("add {0} at {1}",voc,last_row)
        worksheet.update_cell(last_row, 1, voc)
        for i in range(len(chi)):
            worksheet.update_cell(last_row, 2+i, chi[i])
        return True
    else :
        return False
    
def get_word():
    vlists = worksheet.get_all_values()
    print(vlists)
    rand = int(random.random()*len(vlists)-1)
    return vlists[rand]
        



    

    



