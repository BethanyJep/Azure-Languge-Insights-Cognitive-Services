import requests
# %matplotlib inline
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO

subscription_key = "db479bf75e38411891981436d3dcf628"
analyze_url = "https://custom-viznew.cognitiveservices.azure.com//vision/v3.1/analyze"
image_url = "https://c0.wallpaperflare.com/preview/545/533/193/analyzing-people-brainstorming-business-business-people.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'visualFeatures': 'Categories,Description,Faces,Objects'}
data = {'url': image_url}

# try:
response = requests.post(analyze_url, headers=headers,params=params, json=data)
response.raise_for_status()
analysis = response.json()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

# Display the image
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
plt.show()

print(analysis["faces"])