class Product:
    name = 'No name'
    price = '0000'
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def productName(self):
        return self.name
    
    def productPrice(self):
        return self.price
    
    def productInfo(self):
        return f'Product: {self.name}, Price: {self.price}'
    

        