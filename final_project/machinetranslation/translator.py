import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
def englishToFrench(englishText):
    ''' function to translate text in French'''
    model_id = 'en-fr'
    # text_to_translate = englishText
    # Prepare the Authenticator
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01', authenticator=authenticator
    )
    language_translator.set_service_url(url)
    # Translate
    translation = language_translator.translate(text=englishText, model_id=model_id).get_result()
    frenchText = translation["translations"][0]['translation']
    return frenchText


def frenchToEnglish(franchText):
    ''' to translate text in english'''
    model_id = 'fr-en'
    # text_to_translate = englishText
    # Prepare the Authenticator
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01', authenticator=authenticator
    )
    language_translator.set_service_url(url)
    # Translate
    translation = language_translator.translate(text=franchText, model_id=model_id).get_result()
    englishText = translation["translations"][0]['translation']
    return englishText
