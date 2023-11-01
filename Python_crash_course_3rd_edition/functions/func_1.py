def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    print("\n The following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,  completed_models)
show_completed_models(completed_models)


# def print_polyset_son(polyset_sons, new_polyset_sons):
    
#     while polyset_sons:
#         current_polyset_son = polyset_sons.pop()
#         print(current_polyset_son)
#         new_polyset_sons.append(current_polyset_son)


# def show_new_polyset_son(new_polyset_sons):
#     print("The following are the printed polyset sons ")
#     for new_polyset_son in new_polyset_sons:
#         print(new_polyset_son)

# polyset_sons = ['wisdom', 'marvelous', 'miracle', 'melody']
# new_polyset_sons = []

# print_polyset_son(polyset_sons, new_polyset_sons)