key = "xxxx"

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
# region = os.environ['westeurope']
# key = 'db479bf75e38411891981436d3dcf628'
# key = os.environ['db479bf75e38411891981436d3dcf628']

credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(
    endpoint="https://custom-viznew.cognitiveservices.azure.com/",
    credentials=credentials
)

domain = "landmarks"
url = "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg"
language = "en"

analysis = client.analyze_image_by_domain(domain, url, language)

for landmark in analysis.result["landmarks"]:
    print(landmark["name"])
    print(landmark["confidence"])