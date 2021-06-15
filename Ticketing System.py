TICKET_PRICE = 15.00
DISCOUNT = 0.05


def Capture():
    ticket = int(input("Enter number of tickets : "))

    total_price = TicketPay(ticket)
    discount_value = CalcDiscount(total_price)
    nett_pay = NettPay(discount_value, total_price)
    Output(ticket, total_price, discount_value, nett_pay)


def TicketPay(ticket):
    total_price = ticket * TICKET_PRICE
    return total_price


def CalcDiscount(total_price):
    discount_value = total_price * DISCOUNT
    return discount_value


def NettPay(discount_value, total_price):
    nett_pay = total_price - discount_value
    return nett_pay


def Output(ticket, total_price, discount_value, nett_pay):
    print("Payment information :")
    print("Number of tickets : ".format(ticket))
    print("The total price is : RM {:.2f}".format(total_price))
    print("Discount : RM {:.2f}".format(discount_value))
    print("Amount needed to pay : RM {:.2f}".format(nett_pay))


print("~~ Welcome to CFS Ticketing System ~~")
Capture()
