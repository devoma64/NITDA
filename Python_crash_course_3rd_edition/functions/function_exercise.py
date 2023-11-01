
def make_car(manufacturer, model, **other_detials):
    other_detials['manufacturer'] = manufacturer
    other_detials['model'] = model
    
    return other_detials

def build_profile(first, last, **others):
    
    others['first'] = first
    others['last'] = last
    return others

def sandwish_item(**items):
   return items

my_items = sandwish_item(pen='ten', school_fees = 50000, books='twenty')
print(my_items)


my_profile = build_profile('marvelous', 'won', d_o_b = '14-08-1999', location = 'cross river' )
print(my_profile)

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)