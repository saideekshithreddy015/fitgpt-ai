def detect_intent(message):

    message = message.lower()

    food_keywords = ["ate", "eat", "eating", "food", "meal", "breakfast", "lunch", "dinner"]
    workout_keywords = ["walk", "walked", "run", "ran", "running", "cycling", "workout", "exercise", "gym"]
    water_keywords = ["water", "drink", "drank", "hydration"]
    sleep_keywords = ["sleep", "slept", "nap"]
    
    for word in food_keywords:
        if word in message:
            return "food"

    for word in workout_keywords:
        if word in message:
            return "workout"

    for word in water_keywords:
        if word in message:
            return "water"

    for word in sleep_keywords:
        if word in message:
            return "sleep"

    return "chat"