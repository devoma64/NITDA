menu = {
    
    1: {"name": 'espresso',
        "price": 1.99},
    2: {
        "name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4}
}


def calculate_subtotal(order):
    print("printing calculating bills......")
    
    subtotal = 0
    for item in order:
        subtotal += (item['price'])
    return round(subtotal,2)
    
    # raise NotImplementedError()

def calculate_tax(subtotal):
    print("printing calculating tax......")
    
    tax = float(subtotal / 100) * 0.15
    return round(tax,2)
    
    # raise NotImplementedError()
    
def summarize_order(order):
    print_order(order)
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    
    total = round(float(subtotal + tax))
    names = []
    for item in order:
        names.append(item['name'])
        
    return names, total
# function to print out items in an order
def print_order(order):
    
    print('You have ordered ' + str(len(order)) + 'items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# function to display the menu
def display_menu():
    
    print("--------- Menu----------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : > 5}")
    print()
    
# function to creat an order by promting user to select menu items
def take_order():
    
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number' + str(count) + '(from 1 to 5): ')
        count +=1
        order.append(menu[int(item)])
    return order


# some function calls
def main():
    order = take_order()
    print_order(order)
    
    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))
    
    tax = calculate_subtotal(subtotal)
    
    print("Tax for the order is: " + str(tax))
    
    items, subtotal = summarize_order(order)
    
    
if __name__ == "__main__":
    main()
    