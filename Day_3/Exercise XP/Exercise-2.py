# Exercise 2 : Cinemax
family = {}

while True:
    name = input("Input a name (or tape 'done' to quit) : ")
    if name == 'done':
        break
    age = int(input("Input the person\'s name : "))
    family[name] = age

total_cost = 0

for name, age in family.items():
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} must paid {cost}$ for the ticket.")
    total_cost += cost

print(f"The total price of the tickets is {total_cost}$.")