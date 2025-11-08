import os
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = 'API-KEY'

client = OpenAI()

prompt = (
    "A photorealistic image of a ginger dog curled up on a windowsill, "
    "gazing out at a bustling city street slick with rain."
)

response = client.images.generate(
    model="gpt-image-1",   # or "dall-e-3" if your account supports it
    prompt=prompt,
    size="1024x1024",
    n=1
)

print(response.data[0].url)
