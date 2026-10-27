
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

# Create the Gemini client
client = genai.Client(api_key=api_key)

# Send a prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain how AI works in three simple sentences."
)

# Print the model's response
print(response.text)
