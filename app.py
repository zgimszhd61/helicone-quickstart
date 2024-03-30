import os
from helicone.openai_proxy import openai

## https://www.helicone.ai/dashboard

os.environ["HELICONE_API_KEY"] = "sk-"
openai.api_key = "sk-"

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="What is Helicone?",
    user="lininruc@gmail.com" # 可选的Helicone功能
)

print(response.choices[0].text)