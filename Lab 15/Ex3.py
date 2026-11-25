
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = "openrouter/free"

user_messages = "my name is Mahea"
my_messages = [
    {"role": "user", "content": user_messages}
]

response = client.chat.completions.create(
    model=MODEL,
    messages=my_messages
)
print("First response:")
print(response.choices[0].message.content)

second_message = [
    {"role": "user", "content": "What is my name?"}
]

response = client.chat.completions.create(
    model=MODEL,
    messages=second_message
)
print("Second response:")
print(response.choices[0].message.content)