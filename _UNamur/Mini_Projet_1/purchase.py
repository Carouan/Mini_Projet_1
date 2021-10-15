import random

import gaming_tools

def purchase(playername,credit) :
    enough_credit = int(gaming_tools.get_player_money(playername))
    if credit <= enough_credit :
        creaname = gaming_tools.get_random_creature_name()
        creavariety = gaming_tools.get_random_creature_variety()
        creastrength = random.randint(1,credit)
        crealife = random.randint(1, credit)
        print("Your new creature named "+creaname+"!")
        print("Type of the creature : "+creavariety+"")
        txt = "Strength of the creature : {} / [Life] : {}"
        print(txt.format(creastrength, crealife))
        gaming_tools.set_creature(playername, creaname, creavariety, creastrength, crealife)
    else :
         print("You don't have enough money \n")