from flask import Flask, render_template, request, jsonify
# import your model loading code here

app = Flask(__name__)

@app.route('/')
def home():
    # pass companies, years, fuel_types, car_models as context
    return render_template('index.html', companies=..., years=..., fuel_types=..., car_models=...)

@app.route('/predict', methods=['POST'])
def predict():
    # extract form values, process, and return prediction
    return str(predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
