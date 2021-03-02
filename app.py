from flask import Flask, request, jsonify
from predict import predict_sales

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to the Spare Parts Verifier app backend !'


@app.route('/prediction/weekly-sales', methods=['POST'])
def get_prob():
    print('method invoked/ndata retriving')
    user_input = {'Temperature': float(request.form['Temperature']),
                  'Fuel_Price': float(request.form['Fuel_Price']),
                  'CPI': float(request.form['CPI']),
                  'Unemployment': float(request.form['Unemployment']),
                  'Size': float(request.form['Size']),
                  'Type': (request.form['Type']),
                  'Holiday': (request.form['Holiday'])
                  }

    predicted_price = predict_sales(user_input)

    return jsonify({'WeeklySales': round(predicted_price, 2)})


if __name__ == '__main__':
    app.run(debug=any)
