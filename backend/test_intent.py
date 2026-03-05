from app.services.intent_engine import detect_intent

msg1 = "I ate 3 eggs and 2 bananas"
msg2 = "I walked 30 minutes"
msg3 = "I drank 1 liter water"

print(detect_intent(msg1))
print(detect_intent(msg2))
print(detect_intent(msg3))