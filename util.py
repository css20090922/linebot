from flask import Flask, request, abort


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Nwjh3lECegTpMWwZfR2FVFZG4YWdjHb/2IAANyZrtH3a+Vu3+EbXLY+eAm69DyTZZbmiL9A9dpFY0oKao498sDtUOMZdsslsiWYoKa3UTEytkLmsq49Z5jdIs9KrdNZ3TwhlGapC5aWbw/L1NPCj4QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ccdcdf6b37f5f796daaec324d1ef6d99')

from app import *

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
