def print_models(unprinted_designs, completed_models): 
    #move each to completed_models after printing
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        complete_models.append(current_design)

def show_completed_models(completed_models):
    #to print all completed models
    print("\nThe following models have been printed:")
    for complete_model in complete_models:
        print(complete_model)

unprinted_designs = ['iphone', 'robot', 'dodecahedron']
complete_models = []
print_models(unprinted_designs[:], complete_models) #it won't delete the data from the original list (more space)
show_completed_models(complete_models)
