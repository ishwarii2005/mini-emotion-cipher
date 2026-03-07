from langdetect import detect
from deep_translator import GoogleTranslator


def process_text(text):
    """
    Detect language and translate to English if needed.
    Returns translated text.
    """

    try:
        language = detect(text)
    except:
        language = "unknown"

    if language != "en":
        try:
            translated = GoogleTranslator(source="auto", target="en").translate(text)
            return translated
        except:
            return text

    return text