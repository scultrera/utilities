"""
Author: Steve Cultrera
Note: 
- Assumes tesseract has been installed in environment
- You must put pytesseract and PIL in requirements.txt
- io and base64 are part of python


"""

import pytesseract
from PIL import Image
import io
import base64



def load_model(input_dir):
    return "dummy"



def score_unstructured(model, data, query, **kwargs):
    image_string = data
    image_string = io.BytesIO(base64.b64decode(image_string))
    image = Image.open(image_string)
    return pytesseract.image_to_string(image)
    