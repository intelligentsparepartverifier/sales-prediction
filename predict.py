import numpy as np
import pickle

"""# Loading the model for predictions"""

loaded_gbr = pickle.load(open("models/gbrSalesPrediction.pickle.dat", "rb"))

inputData = {'Temperature': 42.31,
         'Fuel_Price': 2.572,
         'CPI': 211.096358,
         'Unemployment': 8.106,
         'Size': 151315,
         'Type': 'A',
         'Holiday': 'No'
         }

input_columns = ['Temperature',
                 'Fuel_Price',
                 'CPI',
                 'Unemployment',
                 'Size',
                 'Type_A',
                 'Type_B',
                 'Type_C',
                 'Holiday_No',
                 'Holiday_Yes']


# input_columns

# setting the inputs to fit the model to predict
def input_to_one_hot(data):
    # initialize the target vector with zero values
    enc_input = np.zeros(10)
    # set the numerical input as they are
    enc_input[0] = data['Temperature']
    enc_input[1] = data['Fuel_Price']
    enc_input[2] = data['CPI']
    enc_input[3] = data['Unemployment']
    enc_input[4] = data['Size']

    ##################### Type #########################
    # redefine the the user inout to match the column name
    redefinded_user_input = 'Type_' + data['Type']
    # search for the index in columns name list
    Type_column_index = input_columns.index(redefinded_user_input)
    # fullfill the found index with 1
    enc_input[Type_column_index] = 1

    ##################### Holiday ####################
    # redefine the the user inout to match the column name
    redefinded_user_input = 'Holiday_' + data['Holiday']
    # search for the index in columns name list
    Holiday_column_index = input_columns.index(redefinded_user_input)
    # fullfill the found index with 1
    enc_input[Holiday_column_index] = 1

    return enc_input


def predict_sales(inputData):
    a = input_to_one_hot(inputData)

    """###Predict"""

    sales_pred = loaded_gbr.predict([a])

    return sales_pred[0]
