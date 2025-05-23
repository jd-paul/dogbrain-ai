from fastapi import APIRouter
from pydantic import BaseModel
import google.generativeai as genai
import os

router = APIRouter()

# Load your key from .env
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define input schema
class DogCoachInput(BaseModel):
    message: str

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

@router.post("/dogcoach")
async def dogcoach_reply(input: DogCoachInput):
    try:
        prompt = f"""
You're a friendly and silly dog named Fifi helping patients.
Speak in a casual, comforting tone with emojis when needed.

Patient: {input.message}
Fifi:"""

        response = model.generate_content(prompt)
        return {"reply": response.text.strip()}

    except Exception as e:
        return {"error": str(e)}
