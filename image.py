# DALL-E 3 requires version 1.0.0 or later of the openai-python library.
import os
from openai import AzureOpenAI
import json

endpoint = "https://ashok-mduk4d5y-swedencentral.openai.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2024-02-01"
model_name = "dall-e-3"
deployment = "dall-e-3"

subscription_key = ""
api_version = "2024-04-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

result = client.images.generate(
    model=deployment,
    prompt="Create a blue flower with honeybee",
    n=1,
    style="natural",
    quality="standard",
)

print(result)

#image_url = json.loads(result.model_dump_json())['data'][0]['url']
#print(image_url)
