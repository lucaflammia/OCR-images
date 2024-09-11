import requests
import json
from io import BytesIO
from PIL import Image
# import url_to_image
import urllib3
import pybase64
import easyocr
from bs4 import BeautifulSoup
from cog import BasePredictor, Input

class Predictor(BasePredictor):

    def predict(self, url: str = Input(description="URL of the image to extract text from")) -> str:
        try:
            # Download and process the image
            # image_file = self.download_image(url)
            encoded_image = self.encode_image(url)
            text = self.ocr_image(encoded_image)

            # Create a structured JSON response
            # result = {
            #     "url": url,
            #     "extracted_text": text,
            # }
            
            return text
            # return json.dumps(result, indent=4)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=4)

    # def download_image(self, url):
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     return BytesIO(response.content)

    def encode_image(self, url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        data = pybase64.b64encode(response.data)
        return data

    def ocr_image(self, url, lang_in: str ='en', lang_out: str ='en'):
        reader = easyocr.Reader([lang_in, lang_out])
        ocr_text = reader.readtext(url)  
        return ocr_text
