# logic/queries/get_translations.py

from utils.translations import translations


def get_translations(lang_code: str) -> dict:
    """
    Returns the full translation dictionary for a given language.
    Falls back to English if the language is not found.
    """
    return translations.get(lang_code, translations["en"])


def get_translation_value(lang_code: str, path: str) -> str:
    """
    Retrieves a nested translation value using dot notation (e.g., 'settings.nav_ui').
    Returns None if the key is not found.
    """
    keys = path.split(".")
    data = get_translations(lang_code)
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data


def get_language_names(lang_code: str) -> dict:
    """
    Returns the localized names of available languages from the 'meta.language_names' key.
    """
    return get_translation_value(lang_code, "meta.language_names") or {}
