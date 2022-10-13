import requests


endpoint = 'http://127.0.0.1:8000/api/products/'                     # Project URL

data = {
    'title': 'Title field Given',
    'price': 11.22
}
get_response_data = requests.post(endpoint, json=data)

""" Prints item inside data """
print(get_response_data.json())                              # Print data in form of Python Dict
