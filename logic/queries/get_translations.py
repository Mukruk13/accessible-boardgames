# logic/queries/get_translations.py

import logging
from utils.translations import translations

logger = logging.getLogger(__name__)

def get_translations(lang_code: str) -> dict:
    """
    Returns the full translation dictionary for a given language.
    Falls back to English if the language is not found.
    """
    if lang_code not in translations:
        logger.debug(f"Language '{lang_code}' not found, falling back to English")
    return translations.get(lang_code, translations["en"])


def get_translation_value(lang_code: str, path: str) -> str | None:
    """
    Retrieves a nested translation value using dot notation (e.g., 'settings.nav_ui').
    Returns None if the key is not found.
    """
    keys = path.split(".")
    data = get_translations(lang_code)
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
            if data is None:
                logger.debug(f"Translation key '{path}' not found for language '{lang_code}'")
                return None
        else:
            logger.debug(f"Unexpected non-dict type encountered at '{key}' for path '{path}'")
            return None
    return data


def get_language_names(lang_code: str) -> dict:
    """
    Returns the localized names of available languages from the 'meta.language_names' key.
    """
    names = get_translation_value(lang_code, "meta.language_names") or {}
    if not names:
        logger.debug(f"Language names not found for language '{lang_code}'")
    return names
