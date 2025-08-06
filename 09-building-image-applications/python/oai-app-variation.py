from openai import OpenAI
import os
from PIL import Image
import dotenv
from security import safe_requests

# import dotenv
dotenv.load_dotenv()

openai = OpenAI()

image_dir = os.path.join(os.curdir, 'images')

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated-image.png')

# ---creating variation below---
try:
    print("LOG creating variation")
    response = openai.images.create_variation(
        image=open("generated-image.png", "rb"),
        n=1,
        size="1024x1024"
    )

    image_path = os.path.join(image_dir, 'generated_variation.png')

    image_url = response.data[0].url

    print("LOG downloading image")
<<<<<<< HEAD:09-building-image-applications/python/oai-app-variation.py
    generated_image = safe_requests.get(image_url).content  # download the image
=======
    generated_image = requests.get(image_url, timeout=60).content  # download the image
>>>>>>> de0a7d07 (Add timeout to `requests` calls):09-building-image-applications/app-variation.py
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()
<<<<<<< HEAD:09-building-image-applications/python/oai-app-variation.py
except openai.InvalidRequestError as err:
    print(err)
=======
except openai.error.InvalidRequestError as err:
    print(err)
<<<<<<< HEAD:09-building-image-applications/python/oai-app-variation.py
>>>>>>> c6871ef1 (Sandbox URL Creation):09-building-image-applications/app-variation.py
=======
>>>>>>> de0a7d07 (Add timeout to `requests` calls):09-building-image-applications/app-variation.py
