

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model (make sure the model file is in the same directory)
model = joblib.load('model.pkl')  # replace 'model.pkl' with the path to your model file

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Extract input data from the JSON request
    marge = data.get('marge')
    liquidite = data.get('liquidite')
    endettement = data.get('endettement')

    # Ensure all inputs are provided
    if marge is None or liquidite is None or endettement is None:
        return jsonify({"error": "All input fields (marge, liquidite, endettement) are required."}), 400

    # Prepare data for prediction as a 2D array (e.g., [[marge, liquidite, endettement]])
    features = [[float(marge), float(liquidite), float(endettement)]]

    # Make prediction
    probability_of_failure = model.predict_proba(features)[0][1] * 100  # Assuming the model returns probabilities

    # Respond with the prediction
    return jsonify({'probabilite': round(probability_of_failure, 2)})

if __name__ == '__main__':
    app.run(debug=True)
