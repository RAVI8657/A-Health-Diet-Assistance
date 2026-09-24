import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

Rs_Token = os.getenv("RS_TOKEN")

client = OpenAI(base_url= "https://router.huggingface.co/v1", api_key = Rs_Token)
response = client.chat.completions.create(model= "openai/gpt-oss-120b", messages= [{
    "role": "user",
    "content": "What is good Source of Protein"
}])

answer = response.choices[0].message.content
print(answer)