import google.generativeai as palm
from dotenv import load_dotenv
import os

api_key = os.environ.get("MODEL_KEY")

def response_AI(prompt):
    palm.configure(api_key=api_key)
    completion = palm.generate_text(
        model="models/text-bison-001",
        prompt=prompt,
        temperature=0,
        max_output_tokens=1000,
    )
    return completion.result
