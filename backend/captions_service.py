from dotenv import load_dotenv
from prompts import caption_prompt
import streamlit as st
import os
from google import genai
import json
from google.genai import types

load_dotenv()

API_KEY = (
    st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
)
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(
    api_key=API_KEY
)


def generate_captions(image_bytes,mime_type):

    image_part = types.Part.from_bytes(
        data = image_bytes,
        mime_type=mime_type
    )

    response = client.models.generate_content(
    model = 'gemini-3.5-flash',
    contents =[
        image_part,
        caption_prompt
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


 