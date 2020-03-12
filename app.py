import os
import sys
import gspread
import re
import datetime
import responses
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError,LineBotApiError 
from linebot.models import *
from SheetMgr import search_word,add_word,get_word
from utils import send_text_message
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

app = Flask(__name__)


adding = False
voc = None
chi = None

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
handler = WebhookHandler(channel_secret)
#圖文選單

img_path="richmenu_1583498398759.jpg"
content_type = "image/jpeg"
rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=2500, height=843),
    selected=False,
    name="小幫手",
    chat_bar_text="Tap here",
    areas=[RichMenuArea(
        bounds=RichMenuBounds(x=1650, y=0, width=843, height=843),
        action=PostbackAction(label='新增單字', data='addvoc'))]
)
richmenu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
with open(img_path, 'rb') as f:
    line_bot_api.set_rich_menu_image(richmenu_id, content_type, f)
    
line_bot_api.set_default_rich_menu(richmenu_id)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global adding,voc,chi
    print(event)
    user_id = event.source.user_id
    text=event.message.text.strip()
    language = isword(text)
    
    
    if adding   :
        
        if text =="不要" :
            reply_text = "已停止新增單字"
            adding = False
        elif(voc == None and language=="english"):
            voc = text.lower()
            print ("enter english")
            reply_text = "新增單字為{}\n請輸入中文，有很多意思的話請用空白隔開".format(voc)
            
        elif (voc !=  None) and  (language !="english"):
            chi = text.split()
            print (str(voc)+str(chi))
            reply_text = "新增單字成功"
            print ("enter chinese")
            successful = add_word(voc,chi)
            adding = False 
            voc = None 
            chi = None
            
            if not successful :
                reply_text = "新增失敗"
        else :
            reply_text = "輸入錯誤\n請重新輸入\n如不要新增請輸入\"不要\""
    else :
        if (text=="小幫手") or (text.lower()=="helper"):
            buttons_template = ButtonsTemplate(
                title='我是小幫手', text='想要幹嘛呢\n要查詢單字請直接輸入文字', actions=[
                    PostbackAction(label='每日一字', data='word'),
                    PostbackAction(label='新增單字', data='addvoc')
                ])
            template_message = TemplateSendMessage(
                alt_text='請用手機看此訊息！', template=buttons_template)
            line_bot_api.reply_message(event.reply_token,  template_message)
            print("小幫手")
        
            return
        elif text == "怎麼用" :
            reply_text = "輸入\"小幫手\"可以叫出小幫手\n直接輸入可以查詢單字\n中英文皆可"
        else:
            reply_text = ""
            print(text.lower())
            res = search_word(text.lower(),language)
            if res!="no result":
                if isword(res) == "other" :
                    for text in res :
                        reply_text += text
                        reply_text += ";"
                    reply_text = reply_text[:-1]
                else:
                    reply_text = res
            else:
                reply_text = res
                    
            
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)
    
#處裡postback的event
@handler.add(PostbackEvent)
def handle_post_message(event):
    global adding
    print("postback")
    print("event =", event)
    times=5
    user_id = event.source.user_id
    action = text=str(str(event.postback.data))
    try:
    #回傳一個單字
        if action == "word" :
            word = get_word()
            text="今天的每日一字為{}，意思是{}".format(word[0],word[1])
    #新增單字
        elif action == "addvoc":
            print("addvoc")
            testing = False
            adding = True
            text="你要新增哪個單字呢\n請先打英文在打中文\n如不要新增請輸入\"不要\""       
        else :
            return
        message = TextSendMessage(text)
        line_bot_api.reply_message(event.reply_token, message)
    except LineBotApiError as e:
        # error handle
        raise e
    
def isword(word) :
    if  word.encode( 'UTF-8' ).isalpha() :
        return "english"
    else :
        return "other"



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
