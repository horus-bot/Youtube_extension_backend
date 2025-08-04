import json
from openai import OpenAI
import os
from dotenv import load_dotenv
from transcription import translation

load_dotenv()

def hindi(url):
    text = translation(url)

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
                    "content": (
                        "You are a translation engine. "
                        "You will receive a JSON array of objects, each with a 'text' field in English. "
                        "Translate ONLY the value of each 'text' field into natural, conversational Hindi. "
                        "Do not change or remove any other keys (such as 'start', 'duration') or their values. "
                        "Keep the JSON array structure exactly the same. "
                        "Return only the modified JSON array with the translated 'text' fields, and nothing else. "
                        "Do NOT include any explanations, markdown, or extra text. "
                        "Return the result as minified JSON (no spaces or line breaks)."
                    ),
                },
                {
                    "role": "user",
                    "content": json.dumps(text),
                },
            ],
            temperature=0.2,
            max_tokens=3000,
        )

        # Parse the response as JSON to ensure it's a valid array/object
        result = response.choices[0].message.content
        try:
            return json.loads(result)
        except Exception:
            # If parsing fails, return the raw result for debugging
            return result

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    translation = hindi()
    print(translation)




