# AI Marketing Copilot

An AI-powered marketing campaign generation API built using Python, FastAPI, and Google's Gemini model.

The application generates structured marketing campaign content based on user-provided inputs, including product details, target audience, campaign goals, social media platform, and preferred tone.

## Features

- AI-powered marketing campaign generation using Gemini.
- Structured JSON responses.
- Input and output validation using Pydantic.
- REST API built with FastAPI.
- Error handling for AI service failures.
- Automated API testing using Pytest.
- Mocked Gemini responses for testing.

## Architecture

The application follows a simple API-based architecture:

1. The client sends campaign details through a POST request.
2. FastAPI receives and validates the input using Pydantic.
3. The application constructs a prompt using the user-provided details and system instructions.
4. The prompt is sent to Google's Gemini model.
5. Gemini generates structured campaign content in JSON format.
6. Pydantic validates the generated response.
7. FastAPI returns the validated campaign as a JSON response.

### Workflow

Client → FastAPI → Input Validation → Gemini → Structured Output → Pydantic Validation → JSON Response

## Project Structure

```text
ai-marketing-copilot/
│
├── api.py              # FastAPI application and API endpoints
├── main.py             # Main application entry point
├── schemas.py          # Pydantic models for input and output validation
├── prompts.py          # System prompt for campaign generation
├── test_api.py         # API endpoint tests
├── test_schema.py      # Schema validation tests
├── .env                # Environment variables (not committed)
├── .gitignore          # Files excluded from Git
└── README.md           # Project document
```

## Tech Stack

- **Python** – Core programming language
- **FastAPI** – Building the REST API
- **Google Gemini** – AI-powered campaign generation
- **Pydantic** – Input and output data validation
- **Pytest** – Automated testing
- **HTTPX** – API testing
- **python-dotenv** – Loading environment variables


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sakshambhardwaj2k5-ux/ai-marketing-copilot.git
```

### 2. Navigate to the project directory

```bash
cd ai-marketing-copilot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```bash
.venv\Scripts\Activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn google-genai python-dotenv pydantic pytest httpx
```


## Environment Setup

### 1. Create a `.env` file in the project root directory.

### 2. Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Replace `your_gemini_api_key_here` with your actual Gemini API key.

**Important:** Never upload your `.env` file or expose your API key on GitHub.


## API Endpoints

### 1. Home

- **Method:** GET
- **Endpoint:** `/`
- **Description:** Checks whether the API is running.

### 2. Health Check

- **Method:** GET
- **Endpoint:** `/health`
- **Description:** Checks the health status of the application.

### 3. Generate Marketing Campaign

- **Method:** POST
- **Endpoint:** `/campaign/generate`
- **Description:** Generates structured marketing campaign content using Google Gemini.

**Request Body:**

```json
{
  "product": "Plant Protein",
  "product_description": "Plant-based protein powder",
  "audience": "Gym beginners",
  "goal": "Increase sales",
  "platform": "Instagram",
  "tone": "Motivational"
}
```

**Response:** Returns structured JSON containing:

- Campaign name
- Key marketing message
- Primary ad copy
- Three social media posts
- Primary call to action
- Influencer brief
- Five hashtags
- Assumptions

## Future Improvements

- Add support for multiple AI models.
- Improve campaign generation with more context-aware prompts.
- Add user authentication and API usage limits.
- Introduce campaign history and database storage.
- Deploy the API to a cloud platform.
