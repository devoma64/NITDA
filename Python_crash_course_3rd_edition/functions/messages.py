def build_profile(first, last, **userinfo):
    
    userinfo['first'] = first
    userinfo['last'] = last
    
    return userinfo
    
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizaa with the following toppings: ")
    
    for topping in toppings:
        print(f"- {topping}")


def send_messages(text_messages, new_messages):
    while text_messages:
        current_message = text_messages.pop()
        print(f"Printing text messages:", current_message)
        new_messages.append(current_message)
       
def show_messages(text_messages):
    print("\n The following text message have been printed")
    for message in text_messages:
        print(message)

        
text_messages = ['I love you Dr. Levista', 'Good morning everyone in this room', 'Hello Mr. Polyset ', 'Good day i am Marvelous Won, a software engineer from spain']

new_messages = []

# send_messages(text_messages, new_messages)
# show_messages(new_messages)

make_pizza(15, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')


user_profile = build_profile('won', 'brainiac', location='cross river', field= 'computer science')

print(user_profile)