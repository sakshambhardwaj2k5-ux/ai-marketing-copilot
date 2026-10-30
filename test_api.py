from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app
from google.genai import errors
from unittest.mock import patch, MagicMock


client = TestClient(app)

def test_home():
    response= client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "The AI Marketing Copilot API is running."
        }

def test_health():
    response=client.get('/health')
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }

def test_create_campaign():
    response=client.post('campaign/generate',json={
        "product": "",
        "audience": "Fitness enthusiasts aged 18–30",
        "goal": "Increase product awareness",
        "platform": "Instagram",
        "tone": "Energetic and motivational",
        "product_description": """
            A plant-based protein powder intended for people who want
            to include plant-derived protein in their daily diet.

            No verified information has been provided about ingredients,
            protein content, flavors, taste, texture, mixability, price,
            certifications, or specific health benefits.
        """
    })
    assert response.status_code == 422





def test_campaign_generation_success():
    fake_campaign = {
        "campaign_name": "Plant Power",
        "key_marketing_message": "Fuel your fitness journey.",
        "primary_ad_copy": "Power your workouts with plant protein.",
        "social_posts": [
            "Post one",
            "Post two",
            "Post three"
        ],
        "primary_cta": "Shop Now",
        "influencer_brief": "Show how the product fits your routine.",
        "hashtags": [
            "#Fitness",
            "#Protein",
            "#PlantBased",
            "#Gym",
            "#Health"
        ],
        "assumptions": []
    }

    fake_response = MagicMock()
    fake_response.parsed = fake_campaign

    with patch("api.client.models.generate_content", return_value=fake_response):
        response = client.post(
            "/campaign/generate",
            json={
                "product": "Plant Protein",
                "product_description": "Plant-based protein powder",
                "audience": "Gym beginners",
                "goal": "Increase sales",
                "platform": "Instagram",
                "tone": "Motivational"
            }
        )

    assert response.status_code == 200
    assert response.json()["campaign_name"] == "Plant Power"

def test_gemini_api_failure():
    with patch(
        "api.client.models.generate_content",
        side_effect=errors.APIError(
            code=500,
            response_json={"error": {"message": "Internal server error"}}
        )
    ):
        response = client.post(
            "/campaign/generate",
            json={
                "product": "Plant Protein",
                "product_description": "Plant-based protein powder",
                "audience": "Gym beginners",
                "goal": "Increase sales",
                "platform": "Instagram",
                "tone": "Motivational"
            }
        )

    assert response.status_code == 502

def test_gemini_returns_no_parsed_data():
    fake_response = MagicMock()
    fake_response.parsed = None

    with patch(
        "api.client.models.generate_content",
        return_value=fake_response
    ):
        response = client.post(
            "/campaign/generate",
            json={
                "product": "Plant Protein",
                "product_description": "Plant-based protein powder",
                "audience": "Gym beginners",
                "goal": "Increase sales",
                "platform": "Instagram",
                "tone": "Motivational"
            }
        )

    assert response.status_code == 502