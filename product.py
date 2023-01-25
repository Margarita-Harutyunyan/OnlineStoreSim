class Product:
    def __init__(self):
        self.__name = 'unknown'
        self.__description = 'no description'
        self.__features = 'no features'
        self.__price = 0
    
    def set_name(self, name):
        self.__name = name 
    def get_name(self):
      return self.__name
    
    def set_description(self, description):
        self.__description = description
    
    def set_features(self, features):
        self.__features = features
    
    def set_price(self, price):
        self.__price = price
    def get_price(self):
      return self.__price
    
    def product_info(self):
      print('Name: {}'.format(self.__name))
      print('Description: {}'.format(self.__description))
      print('Features: {}'.format(self.__features))
      print('Price: {}'.format(self.__price))
    