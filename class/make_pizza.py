def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make. """
    print(f"\nMake a {str(size)}-inch pizza with the followings toppings: ")
    for topping in toppings:
        print(f"- {topping}")