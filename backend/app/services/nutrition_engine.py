import pandas as pd

food_db = pd.read_csv("datasets/global_food_nutrition_350k.csv")

def search_food(food_name):

    result = food_db[
        food_db["food_name"].str.contains(food_name, case=False)
    ]

    if not result.empty:
        return result.iloc[0]

    return None