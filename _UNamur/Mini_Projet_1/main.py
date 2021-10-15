""""
"""
import account, Spurchase

print ("---------------------------------------- \n")
print (" Hi \n Welcome in the mini game from group 18")
print ("---------------------------------------- \n")

# First step : Account creation
playername = input ("Enter your player name : ")
account.player_managment(playername)


# Second step : Purchase or capture a creature
def purchase_or_capture(choice):
    if (choice == "purchase"):
        # appel purchase
        Spurchase.shop(playername)
    elif (choice =="capture") :
        # call capture
        print ("Capture")
    else :
        choice = input("Please enter 'purchase or 'capture'. \n")
        purchase_or_capture(choice)

choice = input ("Would you like to 'purchase' or 'capture' a creature ? \n")
purchase_or_capture(choice)
































#
