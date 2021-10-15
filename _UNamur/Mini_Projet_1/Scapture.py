def capture_creature(playername,credits):
    """
    
    
    
    """

    enough_credit = int(gaming_tools.get_player_money(playername))
    if has_creature(playername)==True 
        print("you already have a creature!")
    else:
        if enough_credit >= 50 
        #capture
            if [random.randint(1, 100)] <= 25 :
                print("You succeeded to capture a creature !")
                creaname = gaming_tools.get_random_creature_name()
                creavariety = gaming_tools.get_random_creature_variety()
                creastrength = random.randint(1,200)
                crealife = random.randint(1,200)
                print("Your new creature named"+creaname+"!")
                print(" Type of the creature :"+creavariety+"")
                txt = " Strength of the creature : {} / [Life] : {}"
                print((txt.format(creastrength, crealife))
            else:
                print("You failed to capture the creature !")
        else: 
            print("You don't have enough credits to capture a creature !")