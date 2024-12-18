from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates')
CORS(app)

model_filename = 'linear_regression_model.pkl'
with open(model_filename, 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

     
        features = [
            "Lot Area", "Overall Qual", "Year Built", 
            "Gr Liv Area", "Garage Area", "Total Bsmt SF"
        ]

      
        if not all(feature in data for feature in features):
            missing = [feature for feature in features if feature not in data]
            return jsonify({"error": f"Missing features: {missing}"}), 400

        
        input_data = pd.DataFrame([data])

        prediction = model.predict(input_data)[0]
        return jsonify({"predicted_price": round(prediction, 2)}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
