from prompts import SYSTEM_PROMPT
import os
from dotenv import load_dotenv
from google import genai
from schemas import CampaignContent

# Load environment variables from .env
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

# Create the Gemini client
client = genai.Client(api_key=api_key)

product = "Plant-based protein powder"
audience = "Fitness enthusiasts aged 18–30"
goal = "Increase product awareness"
platform = "Instagram"
tone = "Energetic and motivational"
product_description = """
A plant-based protein powder intended for people who want
to include plant-derived protein in their daily diet.

No verified information has been provided about ingredients,
protein content, flavors, taste, texture, mixability, price,
certifications, or specific health benefits.
"""

campaign_prompt = f"""

Create marketing campsign using the following inputs:
products: {product}
product description: {product_description}
target audience: {audience} 
campaign goal: {goal}
platform: {platform}
tone: {tone}
"""

# Send a prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    config={'system_instruction': SYSTEM_PROMPT,
            'response_mime_type':'application/json',
            'response_schema': CampaignContent },
    contents=campaign_prompt
)

# Print the model's response
campaign=response.parsed
print(campaign)
print(campaign.model_dump_json(indent=4))