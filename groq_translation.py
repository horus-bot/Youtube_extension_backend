from openai import OpenAI
import os
from dotenv import load_dotenv
from serialize import serial

load_dotenv()

def tamil():
    text = serial()

    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "system",
                    "content": "You are a translation engine. You will receive a JSON array where each object has a 'text' field containing English. Translate ONLY the 'text' field of each object into spoken hindi . Return the modified JSON with translated 'text' fields. DO NOT change other keys. DO NOT summarize. DO NOT respond with anything other than the modified JSON.",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            temperature=0.5,
            max_tokens=3000,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    translation = tamil()
    print(translation)



   
