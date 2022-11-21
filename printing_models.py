# Start with some designs that need to be printed.
unprinted_designs = ['iphone', 'robot', 'dodecahedron']
complete_models = []

#move each to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    complete_models.append(current_design)

#to print all completed models
print("\nThe following models have been printed:")
for complete_model in complete_models:
    print(complete_model)