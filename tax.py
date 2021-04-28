state_tax_rate = {'MA': 0.0625, 'NH': 0, 'ME': 0.055}
state = {'MA','NH', 'ME'}

def calTax(state, receipt):
    tax = 0
    if state == 'MA':
        for i in receipt:
            if receipt[i].type == 'else':
                tax += (receipt[i].cost * receipt[i].quantity * state_tax_rate[state])
    elif state == 'ME':
        for i in receipt:
            if receipt[i].type == 'else' or 'clothing':
                tax += (receipt[i].cost * receipt[i].quantity * state_tax_rate[state])


    return round(tax, 2)
