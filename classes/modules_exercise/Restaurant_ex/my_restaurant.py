from restaurant import Restuarant, IceCreamStand


restaurant = Restuarant("Sweet Cook", "Beans")
ice_cream_stand = IceCreamStand("Marvelous Home", " Delicous Meal", [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Cookies and Cream"
])

ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()


restaurant.describe_restaurant()
