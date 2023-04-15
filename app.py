from flask import Flask, request, jsonify
from model import get_products_needed, pred_best_vals
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.get_json()

    # # Call the Streamlit app's function with the input data
    output_data = get_products_needed([input_data['N'], input_data['P'], input_data['K']], input_data['culture'], input_data['area'])

    best_vals = pred_best_vals(input_data['culture'])
    
    # Return the output data as the response
    return best_vals

if __name__ == '__main__':
    # Start the Flask app
    app.run()
