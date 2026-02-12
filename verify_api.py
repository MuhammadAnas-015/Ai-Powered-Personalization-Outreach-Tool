import os
import sys
import json
from ai_logic import generate_personalized_email

# Ensure .env is loaded
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Mock company data
company_info = {
    "company_name": "TestCorp Solutions",
    "url": "https://testcorp.example.com",
    "description": "We specialize in providing high-end cloud infrastructure for enterprise clients."
}

print(f"Testing Sellable Features (JSON Output) for {company_info['company_name']}...")

try:
    result = generate_personalized_email(company_info)
    
    if isinstance(result, dict):
        print("\nSUCCESS: Received a dictionary response.")
        
        email = result.get('email_body')
        linkedin = result.get('linkedin_note')
        
        print("\n--- COLD EMAIL ---")
        print(email[:100] + "...") # Print preview
        
        print("\n--- LINKEDIN NOTE ---")
        print(linkedin)
        
        if email and linkedin:
             print("\nVERIFICATION PASSED: Both Email and LinkedIn Note generated.")
        else:
             print("\nVERIFICATION FAILED: Missing fields.")
    else:
        print(f"\nFAILURE: Expected dict, got {type(result)}")
        print(result)

except Exception as e:
    print(f"\nFAILURE: Generation failed with error: {e}")
