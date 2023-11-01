def make_shirt(size, text):
    print(f"The size and text on the shirt is: {str(size)} {text}")
make_shirt(45, "Marvelous Won")

make_shirt(size = 45, text="Harmony guidotti")



def display_message():
    return "Everyone i am learning more on python functions"
message = display_message()
print(message)



def favorite_book(title):
    return title
print(favorite_book("One of my favorite books is Alice in Wonderland"))

# making an argument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

developer = get_formatted_name("marvelous", "won")
print(developer)

developer = get_formatted_name("Brainiac", "Harmony", "Guidotti")
print(developer)



def buil_person(first_name, last_name, age= None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person
    else:
        return person
developer = buil_person("marve", "won", 45)
print(developer)


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

while True:
    
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")