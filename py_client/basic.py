import requests


endpoint = 'https://httpbin.org'                        # HTTP Request -> HTML Format
endpoint = 'https://httpbin.org/anything'               # REST API HTTP Request -> Json Format
endpoint = 'http://127.0.0.1:8000/'                     # Project URL

get_response = requests.get(endpoint)                   # HTTP Request

"""
with the following item will come under *data* and,
Content-Type will be application/json  
"""
get_response_data = requests.get(
    endpoint, json={'query': 'Hello Data!'})
"""
with the following item will come under *form* and,
Content-Type will be application/form-urlencoded
"""
get_response_form = requests.get(
    endpoint, data={'query': 'Hello Form Data!'})

# print(get_response_data.text)                                # Print raw text response - Format: Json
print(get_response_form.text)                                # Print raw text response - Format: Json

""" Prints item inside data """
# print(get_response_data.json())                              # Print data in form of Python Dict
""" Prints item inside form """
# print(get_response_form.json())

""" Get status_code of the response"""
# print(get_response_data.status_code)