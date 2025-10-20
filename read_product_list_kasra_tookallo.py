from product_module_kasra_tookallo import *


file = open("product_list_Kasra.dat", "rb")
product_list = pickle.load(file)
file.close()
print(product_list)
show_data(product_list)
