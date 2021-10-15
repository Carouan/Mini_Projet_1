""" Function for purchasing a creature
Parameters
-------------
 credit_purchase : amount of credit chosen for the purchase(int)

Raises
-------
 ValueError : not enough credits for the purchase
 ValueError :  The player already have a creature
Return
-------
 Result : creature_purchase(name_of_creature(str),type_creature(str),strenght_creature(int),life_creature(int))
"""
import gaming_tools, os, random



def amount (playername):
    price = float(input("How much money would you like to spent to purchase a new creature ? \n"))
    if isinstance(price, float):
        purchase (playername,price)
    else:
        price = float(input("Please enter a number only \n"))
        amount(playername)

def purchase (playername,price):
    enough_credit = int(gaming_tools.get_player_money(playername))

    if price <= enough_credit :
        #achat
        creaname = gaming_tools.get_random_creature_name()
        creavariety = gaming_tools.get_random_creature_variety()
        creastrength = random.randint(1, price)
        # set
        crealife = random.randint(1, price)
        # set
        print ("Your new creature named "+creaname+"")
        print (" [Type] : "+creavariety+"")
        txt = " [Strength] : {} / [Life] : {}"
        print(txt.format(creastrength, crealife))
        playermoney = gaming_tools.get_player_money(playername)
        playermoney = (playermoney - price)
        gaming_tools.set_player_money(playername, playermoney)

    else :
        print ("You don't have enough money \n")
        amount(playername)



def shop (playername):
    os.system("cls")
    print ("----------------------------------- \n")
    print ("***  Welcome in the creature Shop  *** \n")
    print ("----------------------------------- \n")
    currentmoney = gaming_tools.get_player_money(playername)
    txt = "       Your fortune : {}                \n"
    print(txt.format(currentmoney))
    amount(playername)
























#
