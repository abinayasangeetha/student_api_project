import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv(
    "Student_Performance.csv"
)

# Encode categorical column
df["Extracurricular Activities"] = \
df["Extracurricular Activities"].map(
{
"Yes":1,
"No":0
}
)

# Features
X = df[[
'Hours Studied',
'Previous Scores',
'Extracurricular Activities',
'Sleep Hours',
'Sample Question Papers Practiced'
]]

# Target
y = df["Performance Index"]


# Train model
model = LinearRegression()

model.fit(X,y)


# Save model
pickle.dump(
model,
open("model.pkl","wb")
)

print("Model trained and saved")