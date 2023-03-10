import requests
import json

from models import Product

class Ordersystem():
    def __init__(self, base_url):
        # Define base URL for API
        self.self.base_url = base_url

    def list_order_list_apis(self):
        """Retrieve a list of all orders"""
        url = f"{self.self.base_url}/ordersystem/api"
        response = requests.get(url)
        return response.json()

    def create_order_list_api(self, data):
        """Create a new order"""
        url = f"{self.base_url}/ordersystem/api"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response.json()

    def retrieve_order_detail_api(self, order_id):
        """Retrieve a specific order by its id"""
        url = f"{self.base_url}/ordersystem/api/{order_id}/"
        response = requests.get(url)
        return response.json()

    def update_order_detail_api(self, order_id, data):
        """Update a specific order by its id"""
        url = f"{self.base_url}/ordersystem/api/{order_id}/"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, data=json.dumps(data), headers=headers)
        return response.json()

    def destroy_order_detail_api(self, order_id):
        """Delete a specific order by its id"""
        url = f"{self.base_url}/ordersystem/api/{order_id}/"
        response = requests.delete(url)
        return response.status_code

    def list_product_list_apis(self):
        """Retrieve a list of all products"""
        url = f"{self.base_url}/ordersystem/api/products/"
        response = requests.get(url)
        return response.json()

    def create_product_list_api(self, data):
        """Create a new product"""
        url = f"{self.base_url}/ordersystem/api/products/"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return Product.update((response.json()))

    def retrieve_product_detail_api(self, product: Product):
        """Retrieve a specific product by its id"""
        url = f"{self.base_url}/ordersystem/api/product/{product.id}"
        response = requests.get(url)
        return product.update(response.json())

    def update_product_detail_api(self, product: Product):
        """Update a specific product by its id"""
        url = f"{self.base_url}/ordersystem/api/product/{product.id}"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, data=json(product), headers=headers)
        return response.json()
