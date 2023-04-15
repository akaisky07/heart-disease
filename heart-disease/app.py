from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)
model = joblib.load("heart_disease_model.joblib")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()
    data = pd.DataFrame([data])
    prediction = model.predict(data)
    if prediction[0] > 0.0:
        result = "Probability: "+str(prediction[0])
    else:
        result = "Probability: "+str(prediction[0])
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)

