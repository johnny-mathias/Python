from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/", methods=['POST'])
def predict():
    data = request.json
    with open("modeloSalario.pkl", "wb") as f:
        model = pickle.load(f.best_estimator)
    return model.predict(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)