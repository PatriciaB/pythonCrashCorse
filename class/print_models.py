"""
Put the functions for the example print_models.py in a separate file called printing_functions.py . 
Write an import statement at the top of print_models.py, and modify the file to use the imported functions 
"""
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm


unprinted_designs = ['iphone', 'robot', 'dodecahedron']
complete_models = []


pm(unprinted_designs[:], complete_models) #it won't delete the data from the original list (more space)
scm(complete_models)