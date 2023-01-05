""" Exercise 4 : FLOATS """
# A foat a type of number. The difference is that it is more qualified as a real while the integer is a positive or negative integer.
# Float can have a comma a power
# Yes we can generate floats using operators on integers
L = list()
U = 4
for i in range(1, 11):
    L.append(U+0.1)
    U += 4
print(L) 
