from app.services.food_nlp_engine import extract_food_items

text = "I ate 3 eggs and 2 bananas"

foods = extract_food_items(text)

print(foods)