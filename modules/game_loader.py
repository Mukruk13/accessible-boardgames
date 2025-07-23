import os
import json


def list_available_games(base_path="data/templates"):
    """
    Zwraca listę ID dostępnych gier (czyli folderów z template.json).
    """
    return [
        name
        for name in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, name))
        and os.path.isfile(os.path.join(base_path, name, "template.json"))
    ]


def get_game_name(game_id, base_path="data/templates"):
    """
    Zwraca nazwę gry (np. 'Czarne Historie') na podstawie ID.
    """
    path = os.path.join(base_path, game_id, "template.json")
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f).get("name", game_id)
    except Exception:
        return game_id


def load_template(game_id, base_path="data/templates"):
    """
    Wczytuje template.json jako słownik.
    """
    path = os.path.join(base_path, game_id, "template.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)
