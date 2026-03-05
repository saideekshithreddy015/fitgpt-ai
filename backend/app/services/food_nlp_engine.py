import spacy
import re

nlp = spacy.load("en_core_web_sm")


def extract_food_items(text):

    doc = nlp(text)
    foods = []
    pattern = r'(\d+)\s+([a-zA-Z ]+)'
    matches = re.findall(pattern, text)
    
    for qty, food in matches:
        foods.append({
            "food": food.strip(),
            "quantity": int(qty)
        })

    return foods