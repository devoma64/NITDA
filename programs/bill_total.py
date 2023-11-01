loyalty_customer = True

bill_total = 124


if loyalty_customer and bill_total > 100:
    # give discount
    bill_total = bill_total - (float(bill_total) / 100) * 20
elif bill_total > 100:
    bill_total = bill_total - (float(bill_total)/100) * 10
    
else:
    # no discount 5% charged applied
    print("Sorry, no discount ....")

print("Total Bill", float(bill_total))
    