import os
import sys
import gspread

import re
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from utils import send_text_message
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
print("line secret  ")
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
handler = WebhookHandler(channel_secret)

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
    print(event)
    user_id = event.source.user_id
    text=event.message.text
    
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    matchChi = zhPattern.search(text)
    if (text=="小幫手"):
        
        buttons_template = ButtonsTemplate(
            title='我是小幫手', text='想要幹嘛呢', actions=[
                PostbackAction(label='每日五字', data='5word',text='每日五字'),
                PostbackAction(label='小測驗', data='exam',text='小測驗'),
                PostbackAction(label='新增單字', data='addvoc',text='新增單字')
                
            ])
        template_message = TemplateSendMessage(
            alt_text='請用手機看此訊息！', template=buttons_template)
        line_bot_api.reply_message(event.reply_token,  template_message)
        print("小幫手")
       
        return
    elif matchChi:
        reply_text = "是中文"
    elif text.encode( 'UTF-8' ).isalpha():
        reply_text = "是英文"
    else:
        reply_text = "亂碼，請重新輸入"
    message = TextSendMessage(reply_text)
    print(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_post_message(event):
# can not get event text
    print("postback")
    print("event =", event)
    line_bot_api.reply_message(
                event.reply_token,
                TextMessage(
                    text=str(str(event.postback.postback.data)),
                )
            )
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
