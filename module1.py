import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key = os.getenv("APIKEY"))


model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Generate me a 2 line tezt introduxing my self")
print(response.text)