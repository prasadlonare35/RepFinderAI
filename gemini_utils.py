import google.generativeai as genai
import os
from typing import List
import json
from dotenv import load_dotenv
import sys

# Print current working directory and env file location
print(f"Current working directory: {os.getcwd()}")
print(f"Looking for .env file in: {os.path.abspath('.env')}")

# Load environment variables
load_dotenv(verbose=True)

# Print all environment variables for debugging
print("Environment variables:", {k: v for k, v in os.environ.items() if 'GEMINI' in k})

# Get API key from environment variable
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("Available environment variables:", list(os.environ.keys()))
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Configure Gemini AI with the API key
genai.configure(api_key=api_key)

async def get_representatives_info(city: str) -> List[dict]:
    """
    Get information about public representatives for a given city using Gemini AI.
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""
        Provide a list of current public representatives (like MPs, MLAs, Municipal Corporation members) 
        for {city}, India. Include their name, designation, phone number, and email if available.
        Format the response as a JSON array with objects containing name, designation, phone, and email fields.
        Provide at least 3-4 representatives. If exact contact details aren't known, you can omit them.
        """

        response = model.generate_content(prompt)
        
        try:
            # Extract JSON from the response
            response_text = response.text
            # Find the JSON part in the response (assuming it's wrapped in ```json ... ```)
            json_start = response_text.find('[')
            json_end = response_text.rfind(']') + 1
            
            if json_start == -1 or json_end == 0:
                # If JSON markers not found, try to parse the entire response
                json_str = response_text
            else:
                json_str = response_text[json_start:json_end]
            
            representatives = json.loads(json_str)
            return representatives
        except json.JSONDecodeError as e:
            # If JSON parsing fails, return a formatted error response
            return [{
                "name": "Error",
                "designation": "Could not parse AI response",
                "phone": None,
                "email": None
            }]
            
    except Exception as e:
        raise Exception(f"Failed to get representatives data: {str(e)}")
