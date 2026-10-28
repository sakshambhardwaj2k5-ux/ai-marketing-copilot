from fastapi import FastAPI,HTTPException
from schemas import CampaignContent, CampaignRequest
from prompts import SYSTEM_PROMPT
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

# Create the Gemini client
client = genai.Client(api_key=api_key)

app = FastAPI(title='AI Marketing Copilot API')

@app.get("/")
def home():
    return {"message": "The AI Marketing Copilot API is running."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
def generate_campaign(response : CampaignRequest)->CampaignContent:
    campaign_prompt=f"""
        Create marketing campsign using the following inputs:
        products: {response.product}
        product description: {response.product_description}
        target audience: {response.audience}
        campaign goal: {response.goal}
        platform: {response.platform}
        tone: {response.tone}
"""
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        config={'system_instruction': SYSTEM_PROMPT,
                'response_mime_type':'application/json',
                'response_schema': CampaignContent },
        contents=campaign_prompt
    )
    if response.parsed is None:
        raise ValueError("Gemini did not return a valid structured campaign")
    return CampaignContent.model_validate(response.parsed)

@app.post('/campaign/generate')
def create_campaign(request: CampaignRequest):
    try:
        return generate_campaign(request)
    except ValueError as error:
        raise HTTPException(status_code=502, detail=str(error))

