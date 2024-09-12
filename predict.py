import requests
import json
import easyocr
from cog import BasePredictor, Input

class Predictor(BasePredictor):

    def predict(self, url: str = Input(description="URL of the image to extract text from")) -> str:
        try:
            # Read image bytes from URL
            image_bytes = self.read_bytes_from_url(url)
            ocr_texts = self.get_ocr_text_from_image(image_bytes)

            # Create a structured JSON response
            result = {
                "url": url,
                "extracted_text": ' '.join(ocr_texts)
            }
            
            return json.dumps(result, indent=4)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=4)

    def read_bytes_from_url(self, url):
        response = requests.get(url)
        image_bytes = response.content

        return image_bytes

    def get_ocr_text_from_image(self, image_bytes, lang_in: str ='en', lang_out: str ='en'):
        reader = easyocr.Reader([lang_in, lang_out])
        outcomes = reader.readtext(image_bytes)
        # readtext outcomes is a list of tuples and only strings are considered for the OCR text
        ocr_texts = [ocr_text for outcome in outcomes for ocr_text in outcome if isinstance(ocr_text, str)]

        return ocr_texts
