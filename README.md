# OCR-Images Project

## Overview

This project extracts text from images using EasyOCR Optical Character Recognition (OCR). It downloads images from a given URL, and then extracts the text using EasyOCR. The project is deployed on [Replicate](https://replicate.com/lucaflammia/OCR-images).

## Usage

You can use this model directly on Replicate:

[**Try it on Replicate**](https://replicate.com/lucaflammia/OCR-images)

### Local Setup (Optional)

If you want to run the project locally:

1. **Install Dependencies:**

   ```bash
   pip install requests easyocr cog
   ```

2. **Run the Predictor:**

   ```python
    from predict import Predictor
    import json

	# Instantiate the Predictor class
	predictor = Predictor()

	# Replace with the actual URL of your PDF
	json_output = predictor.predict(url="https://example.com/your-images.jpeg")

	# Output the full JSON result
	print(json_output)

	# Optionally, parse the JSON to access specific fields
	result = json.loads(json_output)
	print("OCR text : ", result["extracted_text"])
   ```

   This will download the images, extract the text and return the results in JSON format.

## License

This project is licensed under the Apache License Version 2.0.