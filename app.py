from flask import Flask, request, jsonify
import skops.io as sio

app = Flask(__name__)

# Load the model
model = sio.load('RandomForest.skops')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

