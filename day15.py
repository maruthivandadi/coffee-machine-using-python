cup = r"""
        ╔══════════════════════╗
        ║  ██████  Welocome   ███║
        ║  ██████  ████████   ███║════╗
        ║  ██████  ████████   ███║    ║
        ║  ██████  ████████   ███║════╝
        ╚══════════════════════╝
        The Maruthi's Coffee Shop.....
"""

print(cup)



def menu():
    print("==========================The Menu===============================")
  
    menu_dict = {"1 . Espresso" : 40 , "2 . Latte" : 50 ,"3 . chocolate latte" : 60}
    print(menu_dict)

def choice():
    a = int(input("Enter your choice :  "))
    return a 


def get_the_quantity():
    n = int(input("Enter the number of Quantity of cups you required : "))
    return n

#intializing the no.of.cups
cups = 50

bill = 0
shop = True

while shop == True:

    menu()
    print("\n")
    user_choice = choice()
    if user_choice == 1:
        print("Ya thats a good choice")
        ordered_quantity = get_the_quantity()
        cups = cups - ordered_quantity
        bill += (ordered_quantity * 40)
    
    elif user_choice == 2:
        print("Latte a good option")
        ordered_quantity = get_the_quantity()
        cups = cups - ordered_quantity
        bill += (ordered_quantity * 50)
        
    elif user_choice == 3:
        print("cool for chocolate option")
        ordered_quantity = get_the_quantity()
        cups = cups - ordered_quantity
        bill += (ordered_quantity * 60)

    con = input("Do you wanna Continue shopping (y-yes and n-no) : ")
    if con.lower() == "y":
        shop = True
    
    elif con.lower() == "n":
        shop = False
        print(f"Total Bill: ${bill}")
        break


        
