import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Example training data
data = {
    "weight": [70, 75, 68, 80, 65, 72],
    "activity": ["walking", "running", "cycling", "walking", "running", "cycling"],
    "duration_minutes": [30, 20, 45, 40, 15, 60],
    "calories": [120, 210, 300, 180, 160, 420]
}

df = pd.DataFrame(data)

# Convert activity to numeric
df["activity"] = df["activity"].astype("category").cat.codes

X = df[["weight", "activity", "duration_minutes"]]
y = df["calories"]

model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "calorie_model.pkl")

print("Model trained and saved!")