from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("model_params.json", "r") as f:
    params = json.load(f)

@app.route("/", methods=["GET"])
def home():
    return "👋 Hello! Flask API is running. Use POST /predict to get predictions."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    W = data.get("W")
    X_input = data.get("X")
    y_hat = params["const"] + params["W"] * W + params["X"] * X_input
    return jsonify({"predicted_engagement": round(y_hat, 2)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
