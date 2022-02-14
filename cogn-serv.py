key = "ed2d69aba7d048a1b538c72866efb610"
endpoint = "https://learnmoduleworkshop.cognitiveservices.azure.com/"

# from azure.ai.textanalytics import TextAnalyticsClient
# from azure.core.credentials import AzureKeyCredential

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# credential = AzureKeyCredential("ed2d69aba7d048a1b538c72866efb610")
# text_analytics_client = TextAnalyticsClient(endpoint="https://learnmoduleworkshop.cognitiveservices.azure.com/", credential=credential)

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for detecting the language of text
def language_detection_example(client):
    try:
        documents = ["Hello, I would like to take a class at your University. ¿Se ofrecen clases en español? Es mi primera lengua y más fácil para escribir. Que diriez-vous des cours en français?"]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))

def sentiment_anaalysis(client):
    # Get sentiment
    text = ["Smile! Life is good!"]
    sentimentAnalysis = client.analyze_sentiment(documents=text)[0]
    print("\nSentiment: {}".format(sentimentAnalysis.sentiment))

def key_phrases(client):
    #  Get key phrases
    text = ["You must be the change you wish to see in the world."]
    # Get key phrases
    phrases = client.extract_key_phrases(documents=text)[0].key_phrases
    if len(phrases) > 0:
        print("\nKey Phrases:")
        for phrase in phrases:
            print('\t{}'.format(phrase))

def extract_entities(client):
    #  Get key phrases
    text = ["Joe went to London on Saturday"]
    # Get linked entities
    entities = client.recognize_linked_entities(documents=text)[0].entities
    if len(entities) > 0:
        print("\nLinks")
        for linked_entity in entities:
            print('\t{} ({})'.format(linked_entity.name, linked_entity.url))

sentiment_anaalysis(client)
key_phrases(client)
language_detection_example(client)
extract_entities(client)