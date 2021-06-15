COOKING_OIL = 2.50
CURRY_POWDER = 3.40
DETERGENT = 8.50
POTATO_CHIPS = 3.20

a = b = c = d = 0
limit = 1

product = int(input("Enter the number of products that you want to purchase (press 0 to exit) >> "))

while product < 0:
    print("Invalid value!")
    product = int(input("Enter the number of products that you want to purchase (press 0 to exit) >> "))

else:
    if product != 0:
        while limit <= product:
            code = str(input("{:}".format(limit) + "Enter item code of the product that you want to buy >> "))
            quantity = int(input("{:}".format(limit) + "Enter the quantity of product that you want to buy >> "))

            while code != 'a' and code != 'A' and code != 'b' and code != 'B' and code != 'c' and code != 'C' and code != 'd' and code != 'D':
                code = str(input("{:}".format(limit) + " Enter item code of the product that you want to buy >> "))
                quantity = int(input("{:}".format(limit) + " Enter the quantity of product that you want to buy >> "))
            else:
                if code == 'a' or code == 'A':
                    a = a*quantity
                elif code == 'b' or code == 'B':
                    b = b*quantity
                elif code == 'c' or code == 'C':
                    c = c*quantity
                elif code == 'd' or code == 'D':
                    d = d*quantity

            limit = limit+1
        else:
            total_price = COOKING_OIL*a + CURRY_POWDER*b + DETERGENT*c + POTATO_CHIPS*d
            print("The total price is RM {:.2f}".format(total_price))
