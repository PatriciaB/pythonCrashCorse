"""
Put the functions for the example print_models.py in a separate file called printing_functions.py . 
Write an import statement at the top of print_models.py, and modify the file to use the imported functions 
"""

def print_models(unprinted_designs, completed_models): 
    #move each to completed_models after printing
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        


def show_completed_models(completed_models):
    #to print all completed models
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

