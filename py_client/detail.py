import requests


endpoint = 'http://127.0.0.1:8000/api/products/1'                     # Project URL

get_response_data = requests.get(endpoint)

""" Prints item inside data """
print(get_response_data.json())                              # Print data in form of Python Dict
