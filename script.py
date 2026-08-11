import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("GITHUB_TOKEN")
print("Token loaded:", bool(token), "starts with:", token[:8] if token else None)

from openai import OpenAI
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=token
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "hello"}]
)
print(response.choices[0].message.content)