from shopping_cart import *
class User():
    def __init__(self):
        self.__shoppingCart = ShoppingCart()
        self.__balance = 0
    
    def set_balance(self, money):
        self.__balance = money

    def get_balance(self):
        return self.__balance
    
    def add_to_cart(self, product):
        return self.__shoppingCart.addItem(product)
    
    def see_my_cart(self):
        return self.__shoppingCart.seeCart()

    def purchase(self, product):
        price = product.get_price()
        if price > self.__balance:
            print('Not enough money on your balance')
        else:
            self.__balance = self.__balance - price
            print('Item successfully purchased')


