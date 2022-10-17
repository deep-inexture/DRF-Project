import requests


product_id = input('Enter the Product ID :')
try:
    product_id = int(product_id)
except:
    print(f'{product_id} is not valid!')
endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/delete/'                     # Project URL

get_response_data = requests.delete(endpoint)

""" Prints item inside data """
print(get_response_data.status_code, get_response_data.status_code==204)                              # Print data in form of Python Dict
