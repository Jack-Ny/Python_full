""" Exercise 1 : SET """
# Create a set with my favorite number
my_fav_numbers = set()
my_fav_numbers = {1, 6, 4, 8, 3, 12, 22}
# Add two numbers to the set
my_fav_numbers.add(3)
my_fav_numbers.add(11)
# Delete the last number
my_fav_numbers.pop()
# Create a new set
friend_fav_numbers = set()
friend_fav_numbers = {13, 18, 111, 90, 324}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

        
    
