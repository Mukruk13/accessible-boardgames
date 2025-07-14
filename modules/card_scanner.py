import pytesseract
from PIL import Image


def scan_card_image(image_path):
    image = Image.open(image_path)
    raw_text = pytesseract.image_to_string(image, lang='pol')
    return [line.strip() for line in raw_text.strip().split('\n') if line.strip()]


def assign_text_to_fields(text_blocks, fields):
    return {field: text_blocks[i] if i < len(text_blocks) else "" for i, field in enumerate(fields)}
