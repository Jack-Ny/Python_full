def show_magicians(names):
  for name in names:
    print(name)

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Calling the show_magicians() function with the list of magicians' names
show_magicians(magician_names)
def make_great(names):
  for i in range(len(names)):
    names[i] = names[i] + " the Great"

# Calling the make_great() function with the list of magicians' names
make_great(magician_names)
# Calling the show_magicians() function to display the modified list
show_magicians(magician_names)
def make_great(names):
  great_names = [name + " the Great" for name in names]
  return great_names

# Calling the make_great() function to get a new modified list
great_magician_names = make_great(magician_names)

# Calling the show_magicians() function to display the new modified list
show_magicians(great_magician_names)