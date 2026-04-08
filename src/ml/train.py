import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("data/normalized_placement_data.csv")

# Features & target
X = df.drop("Readiness_Score", axis=1)
y = df["Readiness_Score"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("models/regression.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")