from openai import OpenAI
import os
from dotenv import load_dotenv
from transcription import translation

load_dotenv()

def tamil():
    text = translation()

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
                    "content": """You are a translation engine. You will receive a JSON array where each object has a "text" field containing English. 
Translate ONLY the value of the "text" field in each object into natural spoken Hindi. 
Do not modify or remove any other keys ("start", "duration") or their values. 
Preserve the JSON array structure exactly. 
Output only the modified JSON with translated "text" fields and nothing else.
""",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            temperature=0.2,
            max_tokens=3000,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    translation = tamil()
    print(translation)



   
