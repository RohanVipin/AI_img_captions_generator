from dotenv import load_dotenv
from prompts import CAPTION_PROMPT
import os 
from google import genai
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(
    api_key=API_KEY
)

def generate_captions(image_bytes,mime_type):
    response = client.models.generate_content(
    model = 'gemini-3.5-flash',
    contents =[
        {
            'mime_type':mime_type,
            'data':image_bytes
        },
        CAPTION_PROMPT
        ] 
    )

    raw_response = response.text.strip()

    #gemini sometimes wraps json in markdown
    raw_response = (
        raw_response
        .replace("```json","")
        .replace("```","")
        .strip()
    )
    return json.loads(raw_response)


