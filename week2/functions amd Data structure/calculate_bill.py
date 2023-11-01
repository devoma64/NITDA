# function to calculate total tax


def calculate_tax(bill, tax_rate):
    total_bill = (bill * tax_rate) / 100.00
    return round(total_bill, 2)
print('Total bill is: ', calculate_tax(175.00, 15))
print(f'Total bill is: ', calculate_tax(164.33, 22))