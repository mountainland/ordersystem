import json

class Product():
    def __init__(self, id=None, name=None, price=None, visiblity=True):
        self.id = id
        self.name = name
        self.price = price
        self.visiblity = visiblity

    def __json__(self):
        return json.dumps({"id": self.id, "name": self.name, "price": self.price, "visiblity": self.visiblity})

    def update(self, response):
        self.name = response["name"]
        self.price = response["price"]
        self.visiblity = response["visiblity"]