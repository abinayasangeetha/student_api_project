# Feature Login Branchgit add app.py
# Testing git diff
from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained ML model
model = pickle.load(
    open("model.pkl","rb")
)

# Store prediction history
predictions = {}
prediction_id = 1


# --------------------
# HOME (GET)
# --------------------

@app.route("/")
def home():

    return {
        "message":
        "Student Performance API"
    }


# --------------------
# CREATE Prediction (POST)
# --------------------
@app.route("/predict",
methods=["POST"])

def predict():

    global prediction_id

    data = request.json

    features = [[

        data["hours_studied"],
        data["previous_scores"],
        data["extracurricular"],
        data["sleep_hours"],
        data["papers_practiced"]

    ]]

    prediction = model.predict(
        np.array(features)
    )

    result = {

        "id": prediction_id,

        "hours_studied":
        data["hours_studied"],

        "previous_scores":
        data["previous_scores"],

        "predicted_performance":
        round(float(prediction[0]),2)

    }

    predictions[prediction_id] = result

    prediction_id += 1

    return result

@app.route(
"/predictions/<int:id>",
methods=["PUT"]
)

def update_prediction(id):

    if id not in predictions:

        return {
            "message":
            "Prediction not found"
        }

    data = request.json

    predictions[id][
        "hours_studied"
    ] = data["hours_studied"]

    predictions[id][
        "previous_scores"
    ] = data["previous_scores"]

    return {

        "message":
        "Updated",

        "data":
        predictions[id]

    }


# --------------------
# READ ALL (GET)
# --------------------

@app.route("/predictions",
methods=["GET"])

def get_predictions():

    return predictions


# --------------------
# READ ONE (GET)
# --------------------

@app.route("/predictions/<int:id>",
methods=["GET"])

def get_prediction(id):

    if id not in predictions:

        return {
            "message":
            "Not found"
        }

    return predictions[id]


# --------------------
# UPDATE (PUT)
# --------------------


# --------------------
# DELETE
# --------------------

@app.route("/predictions/<int:id>",
methods=["DELETE"])

def delete_prediction(id):

    if id not in predictions:

        return {
            "message":
            "Not found"
        }

    deleted = predictions.pop(id)

    return {

        "message":
        "Deleted",

        "data":
        deleted

    }


if __name__=="__main__":

    app.run(debug=True)