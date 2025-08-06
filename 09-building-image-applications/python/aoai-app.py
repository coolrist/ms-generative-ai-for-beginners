from openai import AzureOpenAI
import os
from PIL import Image
import dotenv
<<<<<<< HEAD:09-building-image-applications/python/aoai-app.py
import json
=======
from security import safe_requests
>>>>>>> c6871ef1 (Sandbox URL Creation):09-building-image-applications/app.py

# import dotenv
dotenv.load_dotenv()

 

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
client = AzureOpenAI(
  api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
  api_version = "2023-12-01-preview",
  azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'] 
  )

model = os.environ['AZURE_OPENAI_DEPLOYMENT']


try:
    # Create an image by using the image generation API

    result = client.images.generate(
        model=model,
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils. It says "hello"',    # Enter your prompt text here
        size='1024x1024',
        n=1
    )

    generation_response = json.loads(result.model_dump_json())
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
<<<<<<< HEAD:09-building-image-applications/python/aoai-app.py
    generated_image = safe_requests.get(image_url).content  # download the image
=======
    generated_image = requests.get(image_url, timeout=60).content  # download the image
>>>>>>> de0a7d07 (Add timeout to `requests` calls):09-building-image-applications/app.py
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
#except client.error.InvalidRequestError as err:
#    print(err)

<<<<<<< HEAD:09-building-image-applications/python/aoai-app.py
finally:
    print("completed!")
=======
# ---creating variation below---

response = openai.Image.create_variation(
  image=open(image_path, "rb"),
  n=1,
  size="1024x1024"
)

image_path = os.path.join(image_dir, 'generated_variation.png')

image_url = response['data'][0]['url']

<<<<<<< HEAD:09-building-image-applications/python/aoai-app.py
generated_image = safe_requests.get(image_url).content  # download the image
=======
generated_image = requests.get(image_url, timeout=60).content  # download the image
>>>>>>> de0a7d07 (Add timeout to `requests` calls):09-building-image-applications/app.py
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

# Display the image in the default image viewer
image = Image.open(image_path)
image.show()
<<<<<<< HEAD:09-building-image-applications/python/aoai-app.py
>>>>>>> c6871ef1 (Sandbox URL Creation):09-building-image-applications/app.py
=======
>>>>>>> de0a7d07 (Add timeout to `requests` calls):09-building-image-applications/app.py
