menu = [
    "espresso",
    "mocha",
    "latte",
    "cappuccion",
    "cortado",
    "americano"
]

def find_coffee(coffee):
    if(coffee[0]) == 'c':
        return coffee
    
# using the map function here
# map_coffee = map(find_coffee, menu)
# print(map_coffee)

# for x in map_coffee:
#     print(x)

# using the filter function here

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for x in filter_coffee:
    print(x)