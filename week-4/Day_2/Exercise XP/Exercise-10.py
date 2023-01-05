"""Exercise 10: SANDWICH ORDERS"""
# List of sandwich
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# creation of empty list
finished_sandwiches = list()
# create "p" which will allow us to determine the exact number of sandwiches prepared
p = 0
# remove ready-made sandwiches
while sandwich_orders !=[]:
    test =input("What sandwich did you finish making?")
    if test in sandwich_orders:
        sandwich_orders.remove(test)
        finished_sandwiches.append(test)
        p = p + 1

# Print the ready-made sandwiches
for i in range(0, p):
    print("I made your",finished_sandwiches[i])