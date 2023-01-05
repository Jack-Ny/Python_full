""" Exercise 3 : LIST """
# Create a list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")
apples = 0
for i in basket:
    if i == "Apples":
        apples = apples + 1
print("There is {} Apples in the basket".format(apples))
basket.clear()
print(basket)