from PIL import Image
import requests
import pytesseract
from io import BytesIO
import json

def main(evt, ctx):
    url = evt["body"]
    res = requests.get(url)
    img = Image.open(BytesIO(res.content))
    txt = pytesseract.image_to_string(img)
    return {"statusCode": 200, "body": json.dumps({
        'txt': txt,
        'key': url,
        'method': 'ocr'
    })}

