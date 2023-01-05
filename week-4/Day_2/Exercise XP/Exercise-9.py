""" Exercise 9 : CINEMAX"""
P=0      # price initialization
nb=int(input("Hello!! How many are you?"))  # family's numbers initialization

# Cost to pay according to the age of the family's members
for i in range(0,nb):

    age=int(input("Enter your person's age: "))
    print("Next person!")
    if age<3:
        # free ticket
        P=P+0
        
    elif 3<age<=12:
        # ticket's price is 10
        P=P+10
        
    elif age>12:
        # ticket's price is 15
        P=P+15    
 
    
print("For all (",nb,") member(s), amount is ",P)



P=0      # price initialization
nb=int(input("Hello! How many are you? : "))  # family's numbers initialization
Name=[]     # list of saved's name
k=nb
#Cost to pay according to the age of the family's members
for i in range(0,nb):
    name=input("Enter your name: ")
    age=int(input("Enter your age : "))
    Name.append(name)
    print("Saved... Pass to the next person")
    
    
    # check age

    if 16<=age<=21:
        # ticket's price is 10
        P=P+10
    else:
        # free ticket
        print("You are not allowed to watch this movie")
        k=k-1
        
        Name.remove(name) # delete the name
           
print(Name)    
print("For all (",k,") member(s), amount is ",P)

