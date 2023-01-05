# module importation
import random

def compare_numbers(num):
  random_num = random.randint(1, 100)
  if num == random_num:
    print("Success ! Two numbers are same : " + str(num) + ".")
  else:
    print("Failed. Two numbers aren\'t same : " + str(num) + " et " + str(random_num) + ".")
compare_numbers(70)