""" Exercise 7 : FAVORITE FRUITS """
fruits = input('Enter your favorite(s) fruits (NB: Separate fruit with a single space): ')
fruits_list  = list()
fruits_list = fruits.split()

my_fruits = input('Enter a fruit name : ')
test = 0
for i in fruits_list:
    if my_fruits == i:
        test = 1

if test == 1 :
    print("You have choose one of your favorite fruits, great !!")
else :
    print("This fruit is not one of your favorite fruits")          
