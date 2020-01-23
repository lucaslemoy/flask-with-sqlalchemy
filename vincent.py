import requests

def get_api_local(product_id):
    param_id = product_id
    result = requests.get(f'http://localhost:5000/products/{param_id}')
    return result.json(), result.status_code

print(get_api_local(1))
