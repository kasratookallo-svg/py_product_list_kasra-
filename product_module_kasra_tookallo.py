import datetime
import re
import pickle



product_list =[]

name = None
brand = None
quantity = 0
price = 0



def data_validation(name, brand , quantity, price, expire_date):

    if re.match(r"^[a-zA-Z]{2,20}$", name) and re.match(r"^[a-zA-Z]{2,20}$", brand) and quantity > 0 and price > 0 and expire_date > datetime.date.today():
        return True
    else:
        return False

def get_data ():
    name = input("Enter your good name: ")
    brand = input("Enter your good brand: ")
    price = int(input("Enter your good price: "))
    quantity = int(input("Enter your good quantity: "))
    expire_date = input("Enter your good expire date: (year/month/day) ")
    expire_date = datetime.datetime.strptime(expire_date, "%Y/%m/%d").date()

    if data_validation(name, brand , quantity, price , expire_date):
        product = {"name":name , "brand":brand , "quantity": quantity , "price": price , "expire date":expire_date }
        return product
    else:
        print("Invalid data!!!")
        return None


def save_to_file (product_list):
    file = open("product_list_Kasra.dat", "wb")
    pickle.dump(product_list, file)
    file.close()

def show_data(product_list):
    for product in product_list:
        print(f"{product['name']:10}  -  {product['brand']:10} - ( Tedad :{product['quantity']:>3}) (Price :{product['price']:>8})")

