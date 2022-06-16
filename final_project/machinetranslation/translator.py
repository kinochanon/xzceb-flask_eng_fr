"""This module is a wrapper around IBM's Watson Language Translation API."""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    """Return French translation of an english word/phrase."""

    if not englishText:
        return ''

    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation'] if translation is not None else ''

def frenchToEnglish(frenchText):
    """Return English translation of a french word/phrase."""

    if not frenchText:
        return ''

    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation'] if translation is not None else ''

if __name__ == '__main__':
    test = englishToFrench('Hello')
    print(test)
    