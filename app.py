from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import datetime
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join("model", "model.pkl")
model = None
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        appliances = data.get("appliances", [])
        price_per_unit = float(data.get("price_per_unit", 0))

        # 1. Deterministic Calculation: sum of (watt * hours) / 1000
        total_consumption_kwh = sum([(float(app.get("watt", 0)) * float(app.get("hours", 0))) / 1000 for app in appliances])
        
        # 2. Predictive Modelling
        # total_load is required by the model (we used Watt instead of kW for total_load in features)
        total_load_watts = total_consumption_kwh * 1000
        
        now = datetime.datetime.now()
        # For a more specific demo, we use current time, but it could be user input
        hour_of_day = now.hour
        day = now.day
        month = now.month
        
        if model is not None:
            # Model features: [total_load, hour_of_day, day, month]
            features = np.array([[total_load_watts, hour_of_day, day, month]])
            predicted_consumption_kw = float(model.predict(features)[0]) # Global active power in kW
            # Use predicted consumption if valid, otherwise fallback to deterministic
            final_consumption_kwh = max(0, predicted_consumption_kw)
        else:
            final_consumption_kwh = total_consumption_kwh
            
        # Estimated cost
        estimated_cost = final_consumption_kwh * price_per_unit

        return jsonify({
            "success": True,
            "deterministic_consumption_kwh": round(total_consumption_kwh, 2),
            "predicted_consumption_kwh": round(final_consumption_kwh, 2),
            "estimated_cost": round(estimated_cost, 2),
            "breakdown": [ {
                "name": app.get("name"), 
                "consumption": round((float(app.get("watt", 0)) * float(app.get("hours", 0))) / 1000, 2)
            } for app in appliances ]
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
