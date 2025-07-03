import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("OPENAI_API_BASE"))

def summarize_text(text):
    prompt = "Summarize the following notes or textbook content into key bullet points with the most important information:\n" + text

    response = client.chat.completions.create(
        model="mistralai/mixtral-8x7b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
