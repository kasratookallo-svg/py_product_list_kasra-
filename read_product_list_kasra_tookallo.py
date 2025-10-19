from product_module_kasra_tookallo import *


file = open("product_list_Kasra.dat", "rb")
product_list = pickle.load(file)
file.close()
print(product_list)
for product in product_list:
    print(
        f"{product['name']:10}  -  {product['brand']:10} - ( Tedad :{product['quantity']:>3}) (Price :{product['price']:>8})")

