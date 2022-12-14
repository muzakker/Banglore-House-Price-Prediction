import json
import pickle
import numpy as np

# to save the artifacts into global variables
__locations = None
__data_columns = None
__model = None

# writing a function to get the estimated price
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

# creating a new file called util, and util will contain all the core routines whereas the server will do the routing of request and response
def get_location_names():
    return __locations

# to load the artifacts (columns.json and the pickle file)
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    # loading json artifact
    with open("./artifacts/columns.json", 'r') as f:
        # to convert the json objects into a dictionary
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:] # because location starts from 3rd index
    
    global __model
    # loading pickle file
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f: # rb because its a binary model
        __model = pickle.load(f)
    
    print("loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2)) # other location