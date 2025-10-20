from product_module_kasra_tookallo import *

#Variants
product_list = []
total_price = 0
majmoo = 0

#Unlimited cycle until
while total_price < 1000000:

    #First function for entering data from operator
    product = get_data()
    total_price += product['price'] * product['quantity']
    if total_price < 1000000:

        #creating the product_list
        product_list.append(product)

        #Second function as pickle
        save_to_file(product_list)
        print("product saved")
        print("-"*100)
    else:
        print("You have reached the peak!!!")

#Third function
show_data(product_list)

#Calculating the total price
for product in product_list:
    majmoo += product['price']*product['quantity']
print("Total amount of prices is ", majmoo)

print("-"*100)

#todo here is only one problem, that if operator enter incorrect name and brand, suddenly the program shows "Invalid data!!!" and stops working.
#todoدر صورتیکه کاربر اطلاعات نام و برند محصول را اشتباه وارد کند، اخطار متنی پاسخ میدهد و سپس متوقف میشود.1



