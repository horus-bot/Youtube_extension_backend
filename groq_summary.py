from openai import OpenAI
import os
from dotenv import load_dotenv
from transcription import  subtit

load_dotenv()

def groq_summary(url):
    text = subtit(url)

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
                    "content": "You are a YouTube video summarizer. Provide a extensive detailed report of the video where you will create a summary and then followup by giving details and explaining everything.Reply only in english no special character",
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
    summary = groq_summary(input("url"))
    print("\n Video Summary:\n")
    print(summary)

   
