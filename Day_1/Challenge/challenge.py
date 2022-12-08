# > <
import random
texte = str(input('Put the string (10 characters) \t: '))
size = len(texte)
# Convert the string to list    
str_var = list(texte)
# Then shuffle the string contents and will print the string    
random.shuffle(str_var)
if size > 10 :
    print('String too long')
elif size  < 10 :
    print('String not long enough')
if size == 10 :
    for i in range(size) :
    # i + 1 before the last character
        print(texte[: i + 1])
print (''.join(str_var))                            


