from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

pipeline = joblib.load('model/logistic_regression_model.pkl')

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json(force = True)
    df = pd.DataFrame(data)
    predictions = pipeline.predict(df)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host = '0.0.0.0')

