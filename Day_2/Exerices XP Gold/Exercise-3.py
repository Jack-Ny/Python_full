names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
pt = 0
name = input('Enter your name : ')
for i in names:
    if (i == name):
        pt = 0       
if pt != 0:
    print("Your name {} is in position {} ".format(name, pt))
else :
    print("Your name is not on the list")          
