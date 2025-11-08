import os
from openai import OpenAI
import requests
import shutil
from PIL import Image

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

image_url = response.data[0].url

print(response.data[0].url)

image_resource = requests.get(image_url, stream=True )
# print image url status code

if image_resource.status_code == 200:
    image_name = 'dalle-ginger-dog.png'
    with open(image_name, 'wb') as f:
        shutil.copyfileobj(image_resource.raw, f)
else:
    print('error accessing image')

Image.open(image_name)