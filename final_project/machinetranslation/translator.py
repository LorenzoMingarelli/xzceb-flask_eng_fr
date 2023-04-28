''' Translate text using IBM Watson LanguageTranslatorV3'''
import os
from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Translate text from english to french using LanguageTranslatorV3'''
    if(english_text and english_text != ''):
        french_text = ''

        try:
            french_text = language_translator.translate(
                text=english_text,
                model_id='en-fr'
            ).get_result()
        except ApiException as ex:
            print("Translation method failed with status code " + str(ex.code) + ": " + ex.message)

        return french_text["translations"][0].get("translation")

    return 'ERROR: Text must be provided'

def french_to_english(french_text):
    ''' Translate text from french to english using LanguageTranslatorV3'''
    if(french_text and french_text != ''):
        english_text = ''

        try:
            english_text = language_translator.translate(
                text=french_text,
                model_id='fr-en'
            ).get_result()
        except ApiException as ex:
            print("Translation method failed with status code " + str(ex.code) + ": " + ex.message)

        return english_text["translations"][0].get("translation")

    return 'ERROR: Text must be provided'
