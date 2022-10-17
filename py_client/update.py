import requests


endpoint = 'http://127.0.0.1:8000/api/products/1/update/'                     # Project URL

data = {
    'title': 'Hello World! You are updated',
    'price': 111.1
}
get_response_data = requests.put(endpoint, json=data)

""" Prints item inside data """
print(get_response_data.json())                              # Print data in form of Python Dict
