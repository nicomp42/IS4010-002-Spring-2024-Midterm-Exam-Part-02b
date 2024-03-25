# phoneClass.py

class Phone:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        
    def getModel(self):
        return self.model
    
    def getPrice(self):
        return self.price