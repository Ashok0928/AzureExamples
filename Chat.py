import os
from openai import AzureOpenAI

endpoint = "https://aiaihub8622302327.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2025-01-01-preview"
model_name = "gpt-4o-mini"
deployment = "gpt-4o-mini"

subscription_key = "A7juCThUzhOUj5kefy0KvGdvHCqPa5m9IJyXlXoZ3zx1LjdKdWODJQQJ99BGACHYHv6XJ3w3AAAAACOGYlLW"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Where is Charlotte?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)
print(response.choices[0].message.content)





