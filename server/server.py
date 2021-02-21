import pickle
import numpy as np
from flask import Flask, request

model = None
app = Flask(__name__)


def load_model():
    global model

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


@app.route('/')
def home_endpoint():
    return 'Welcome to the Phishing Detection Server!'


def predict(data):
    data = np.array(data)[np.newaxis, :]

    # runs globally loaded model on the data
    prediction = model.predict(data)

    return prediction


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single point

    data = request.get_json()  # Get data posted as a json

    prediction = predict(data)

    return str(prediction[0])


@app.route('/multi-predict', methods=['POST'])
def get_multiple_prediction():
    # Works only for multiple points

    predictions = []

    data = request.get_json()  # Get data posted as a json
    print(data)

    for point in data:

        prediction = predict(point)

        predictions.append(str(prediction[0]))

    return predictions


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
