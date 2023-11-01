
# Let's say you want to give a certain discount to customers if they spend over $100. 
# You will also provide an extra discount if that customer is part of a loyalty program. 
# If the customer is not part of the loyalty program and did not spend over a $100, a service charge of 5% is applied.


loyal_customer = True
bill_total = 124

if loyal_customer and bill_total > 100:
    # give our loyalty customer discount of 20%
    bill_total = bill_total - (float(bill_total)/100) * 20
    
elif bill_total > 100:
    # give the customer discount of 10%
    bill_total = bill_total - (float(bill_total) /100) *10
    
else:
    # no discount applied
    print("sorry no disccount...")
    
print("Bill Total: ", float(bill_total))