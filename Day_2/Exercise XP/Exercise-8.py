""" Exercise 8: WHO ORDERED A PIZZA ?"""
L = list()
p = 0
while True:
    pizzas = input('Enter a pizza(s) topping (or tape quit to cancel): ')
    if pizzas != 'quit':
        L.append(pizzas)
        print("You add {} to the pizza\'s topping list ".format(pizzas))
        p = p + 2.5
    else:
        pizzas = ""
        break    
print("All topping : ", L, "\n", "The total price of this pizza with all topping are :", 10+p)