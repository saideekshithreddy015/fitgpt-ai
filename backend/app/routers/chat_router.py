from fastapi import APIRouter
from services.intent_engine import detect_intent
from services.food_nlp_engine import extract_food_items
from services.workout_engine import predict_calories

router = APIRouter()

@router.post("/chat")
def chat(message: str, weight: float ):

    intent = detect_intent(message)

    if intent == "food":

        foods = extract_food_items(message)

        return {
            "intent": "food",
            "foods_detected": foods,
            "message": "Food logged successfully"
        }

    elif intent == "workout":

        duration = 30
        calories = predict_calories(weight, "walking", duration)

        return {
            "intent": "workout",
            "calories_burned": calories,
            "message": "Workout logged"
        }

    else:

        return {
            "intent": "chat",
            "message": "Tell me about your workout or meals today!"
        }