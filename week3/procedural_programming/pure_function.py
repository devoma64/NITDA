my_list = [1,2,3]

# creating a pure function


# def add_to_list(lst, item):
#     nl = lst.copy()
#     nl.append(item)
    
#     return nl
# new_list = add_to_list(my_list, 4)

# print(my_list)
# print(new_list)




def lets_add_to_the_list(the_list, item_to_be_added):
    # making a duplicate of the list given
    copied_list = the_list.copy()
    
    # appending the item to the copied list to avoid mutability on the original list
    copied_list.append(item_to_be_added)
    
    # now lets return our copied list
    return copied_list
# lest pass in the new item to be added to our list

new_list = lets_add_to_the_list(my_list, 4)
# first lets print our orinal list to be sure it was immutable 
print(my_list)

# now lets print our new list

print(new_list)

# So the function above lets_add_to_the_list() is called a pure function


# well now lets create a regular function that will do the same work but the mylist will be mutable in this case

def add_to_list(item):
    return my_list.append(item)
add_to_list(4)

print(my_list)