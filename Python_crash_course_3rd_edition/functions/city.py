
def city_country(country_name, country_city):
    country_info = f"{country_name}, {country_city}"
    return country_info

while True:
    print("Please tell me your country name and city")
    
    c_city = input("\nEnter country city: ")
    c_name = input("\nEnter country name: ")
    break
    
country_details = city_country(c_city, c_name)
print(f"\nMy country name and city is: {country_details}")