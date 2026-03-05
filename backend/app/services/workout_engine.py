import os
import joblib

# Get absolute path to the ML model
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "calorie_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_calories(weight, activity, duration):

    activity_map = {
        "walking": 0,
        "running": 1,
        "cycling": 2
    }

    activity_code = activity_map.get(activity.lower(), 0)

    prediction = model.predict([[weight, activity_code, duration]])

    return round(float(prediction[0]), 2)