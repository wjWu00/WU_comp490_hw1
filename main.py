# Weijing Wu
# COMP 490 HW1

import product
import tax

invalid_input = True
while invalid_input:
    state = input("Which state are you? (MA, NH, ME): ").upper()
    if state not in ('MA', 'NH', 'ME'):
        invalid_input = True
    else:
        invalid_input = False
spend = 0
order = 0
total_tax = 0
receipt = {}  # create a dictionary to later get the total list
buy = True
while buy:
    invalidgrp_id = True
    while invalidgrp_id:
        buy_id = int(input("Please enter your item ID: "))
        if buy_id in product.productlist:
            invalidgrp_id = False
        else:
            invalidgrp_id = True
            print("Sorry. This item is not available!")
    quantity = int(input("Please enter your item quantity: "))
    order = order + 1
    # make call to product class
    item_id = product.productlist[buy_id].id
    item_type = product.productlist[buy_id].type
    item_name = product.productlist[buy_id].name
    item_cost = product.productlist[buy_id].cost
    total_cost = product.productlist[buy_id].cost * quantity
    spend = spend + total_cost
    # setup the receipt
    receipt[int(order)] = product.Receipt(item_id, item_type, item_name, item_cost, quantity)
    total_tax = tax.calTax(state, receipt) # call tax class
    total_price = spend + total_tax
    buymore = input("Continue Shopping? (Y = Yes/N = No): ").upper()
    if buymore == 'Y':
        buy = True
    else:
        buy = False  # while loop ends, user stop buying, user want to see total money spent
        print("Your Total is:", round(total_price, 2))

        payment = input("Do you want to pay with Cash or Card? (1 = Cash, 2 = Credit/Debit Card)")
        if payment == '1':
            wrong_amount = True
            while wrong_amount:
                money_pay = float(input("How much are you paying?: "))
                if money_pay < (total_price):
                    wrong_amount = True
                    print("Sorry! Your total is ", round(total_price, 2))
                else:
                    wrong_amount = False
                print("You Pay Cash       $", money_pay)  # collecting cash amount
                print("Change due         $", round(money_pay - spend - total_tax, 2))  # make change
        else:
            card = input("Please enter your credit/debit card number: ")
            print("You have paid $", round(total_price, 2), "from your card!")


        print("\n\t***YOUR RECEIPT***\n")
        for x in receipt:
            print(str(x) + ')', receipt[x].name, '--', receipt[x].cost, "  Quantity:", receipt[x].quantity, "--", round(receipt[x].quantity * receipt[x].cost, 2))
        print("Subtotal:          $", spend)
        print(state, " Tax ", tax.state_tax_rate[state]*100, '%', "    $", total_tax)
        print("Total              $", round(total_price, 2))

        print("\n***Thank You For Shopping Here!***")
