import os
import openai

openai.api_key = os.getenv("OPENAI_KEY")

def generate_response(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
        temperature=0.5
    )

    return response