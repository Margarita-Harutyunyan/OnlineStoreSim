from user import *

me = User()
notebook = Product()
me.set_balance(565)
notebook.set_price(344)
notebook.set_name('Notebook')
notebook.set_description('For writing')
nb = {'Color' : 'Blue', 'Page number' : 96, 'Page view' : 'Squared'}
notebook.set_features(nb)
notebook.product_info()
me.add_to_cart(notebook)
me.add_to_cart(notebook)
print(me.see_my_cart())
me.purchase(notebook)
me.purchase(notebook)
