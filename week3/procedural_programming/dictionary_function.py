#Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("using range(): ", usingrange)

#working with lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

#Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)


# Using two input lists
# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)
months_dictionaary = {key:value for (key, value) in zip(number, months)}
print(months_dictionaary)


# Set comprehension
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
print(set_a)