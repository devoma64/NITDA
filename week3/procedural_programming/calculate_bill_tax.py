food_bill = {
    1: 3.99,
    2: 4.55,
    3: 11.99,
    4: 22.00,
    5: 2.00
}


def bill_total(bill):
    total_bill = 0.00
    
    for x, y in  bill.items():
        total_bill += y
    return total_bill

def calculate_tax(percent, bill_total):
    tax = (percent * bill_total) / 100.0
    return round(tax,2)


total_food = bill_total(food_bill)
tax_total = calculate_tax(15, total_food)

print(total_food)
print(tax_total)

overall_total = total_food + tax_total
print("The overall total is: ", overall_total)
# def bill_total(bill):
#     total_bill  = 0.00
#     for k, v in bill.items():
#         total_bill += v
#     return total_bill


# def calculate_tax(percent, bill_total):
#     tax = (percent * bill_total) / 100.0
#     return round(tax,2)

# food_total = bill_total(food_bill)
# tax_total = calculate_tax(15, food_total)

# print("overall:", food_total + tax_total)