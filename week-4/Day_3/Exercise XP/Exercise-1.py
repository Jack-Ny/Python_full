# Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# with a dictionary comprehension
    #dictionary = { key: value for key, value in zip(keys, values)}
# with dict constructor
dictionary = dict(zip(keys, values))
print(dictionary)