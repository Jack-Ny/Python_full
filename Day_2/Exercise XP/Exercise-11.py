""" Exercise 11 : SANDWICH ORDERS 2"""

sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = list()
p = 0
print("ALERT!!! Charcuterie no longer has pastrami")


# pastramis delete
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders != [] :
    test = input("What sandwich did you finish making? ")
    if test in sandwich_orders:
        sandwich_orders.remove(test)
        finished_sandwiches.append(test)
        p = p + 1

# print the finished sandwich without pastramis
for i in range(0, p):
    print("I made your",finished_sandwiches[i])