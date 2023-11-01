for i in range(21):
    print("Looping....", i)
    
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']


# for item in favorites:
#     print('I like this desert', item)

# Looping through the same array using while loop

count = 0

while count < len(favorites):
    print("I like this desert", favorites[count])
    count += 1
    
for idx, item in enumerate(favorites):
    print(idx, item)