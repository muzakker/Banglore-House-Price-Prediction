from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods = ['GET']) # to expose http endpoint, meaning we do not want to get 404 error

# to return all the  locations in our UI
def get_location_names():
    # jsonify method to return all the locations
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods = ['GET', 'POST'])
def predict_home_price():
    # storing the values from Post method to local variables
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug = True)