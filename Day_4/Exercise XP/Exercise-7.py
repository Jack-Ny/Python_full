import random

def get_random_temp():
    return random.uniform(-10, 40)

for i in range(10):
    print(get_random_temp())

import random

def get_random_temp():
    return random.randint(-10, 40)


#############################################################
def main():
    # Obtaining a random temperature
    temp = (get_random_temp())
    
    print(f"The current temperature is {temp} degrees Celsius.")
    
       
main()


###############################################################################
import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()

    if temp < 0:
        print(f"it's freezing cold! Wear extra layers today. The current temperature is {temp} degrees Celsius.")
    elif temp >= 0 and temp <= 16:
        print(f"Pretty cold! Don't forget your coat. The current temperature is {temp} degrees Celsius.")
    elif temp > 16 and temp <= 23:
        print(f"It's cool. Remember to put on a sweater. The current temperature is {temp} degrees Celsius.")
    elif temp > 23 and temp <= 32:
        print(f"The weather is nice. Don't forget to take a jacket if you go out. The current temperature is {temp} degrees Celsius.")
    elif temp > 32:
        print(f"It's hot! Don't forget to drink water and put on sunscreen. The current temperature is {temp} degrees Celsius.")

main()



################################################################

import random

def get_random_temp(saison):
  if saison == "été":
    lower_bound = 16
    upper_bound = 40
  elif saison == "automne" or saison == "printemps":
    lower_bound = -10
    upper_bound = 16
  elif saison == "hiver":
    lower_bound = -10
    upper_bound = 16
  else:

    lower_bound = -10
    upper_bound = 40

  return random.randint(lower_bound, upper_bound)

def main():

  saison = input("Enter a season (été, automne, hiver, printemps) : ")

  temp = get_random_temp(saison)
  print("The temperature is", temp, "degrees.")

main()



################bonus 1 ##############
def main():

  saison = input("Saisissez une saison (été, automne, hiver, printemps) : ")
  temp = get_random_temp(saison)
  print("La température est de", temp, "degrés.")

main()
#################################

def main():
  mois = int(input("Saisissez le numéro du mois (1-12) : "))

  if mois == 12 or mois == 1 or mois == 2:
    saison = "hiver"
  elif mois >= 3 and mois <= 5:
    saison = "printemps"
  elif mois >= 6 and mois <= 8:
    saison = "été"
  elif mois >= 9 and mois <= 11:
    saison = "automne"
  else:
    saison = "hiver"

  temp = get_random_temp(saison)
  print("La température est de", temp, "degrés.")

main()