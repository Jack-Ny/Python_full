def make_shirt(size, text):
  print("The size of the shirt is " + size + " and the text is '" + text + "'.")

# call of make_shirt's function with parameters
make_shirt("medium", "I love Python")
def make_shirt(size="large", text="I love Python"):
  print("The size of the shirt is " + size + " and the text is '" + text + "'.")

# Make a shirt with the default's message
make_shirt()

# Make a moyen shirt with the default's message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", text="I love coding")