# logic/queries/get_translations.py

from utils.translations import translations

def get_translations(lang_code):
    """Returns full translation dict with fallback to English."""
    return translations.get(lang_code, translations["en"])

def get_translation_value(lang_code, key):
    """Returns a specific value from the translation dict."""
    return get_translations(lang_code).get(key)

def get_language_names(lang_code):
    """Returns the language_names mapping from a given language."""
    return get_translation_value(lang_code, "language_names") or {}
