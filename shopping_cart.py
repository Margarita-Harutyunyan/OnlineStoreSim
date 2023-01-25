from product import *

class ShoppingCart():
    def __init__(self):
        self.__products = []
    
    def addItem(self, product):
        name = product.get_name()
        self.__products.append(name)
    
    def seeCart(self):
        return self.__products
  
