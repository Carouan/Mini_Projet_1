import account
import gaming_tools, random



def evolution(creature,credit):

    if gaming_tools.creature_exists(creature):

        # If you want to change the cost of evolution
        cout_evo = 10
        # Get player name and player money
        player = gaming_tools.get_player(creature)
        playermoney = gaming_tools.get_player_money(player)


        if credit >= cout_evo:
            # Get actuel strength and life of the creature.
            strength = gaming_tools.get_creature_strength(creature)
            s =strength
            life = gaming_tools.get_creature_life(creature)
            l = life
            # Current Strength Bonus
            global cSB
            cSB = 0
            # Current Life Bonus
            global cLB
            cLB = 0

            nbr_evo = (int(credit/cout_evo))
            nbr = nbr_evo

            if nbr >= 1:
                result_evo(nbr)
                # Calculate the money of the player after nbr_evo
                rest = (int(credit % cout_evo))
                playermoney = playermoney - (nbr_evo * cout_evo) + rest
                gaming_tools.set_player_money(player, playermoney)

                strength = strength + cSB
                life = life + cLB
                gaming_tools.set_creature_strength(creature, strength)
                gaming_tools.set_creature_life(creature, life)

                newstrength = gaming_tools.get_creature_strength(creature)
                newlife = gaming_tools.get_creature_life(creature)
                print("\033[0;32m***  EVOLUTION  ***\033[00m")
                txt = "\033[0;32m*\033[00m Your creature " + creature + " has evovled {} times.\n\033[0;32m*\033[00m And get +{} points of strength and +{} points of life."
                print(txt.format(nbr_evo, cSB, cLB))
                txt = "\033[0;32m*\033[00m [Strength]({}+{}) : {} // [Life]({}+{}) : {} "
                print(txt.format(s,cSB,newstrength,l,cLB,newlife))
                txt = "\033[0;32m*\033[00m You have {} credits left."
                print(txt.format(playermoney))
                print("\033[0;32m*******************\033[00m")
        else:
            print("You don't have enough money to evoluate your creature!")
    else :
        print("\033[0;31m   => This creature can't evolve 'cause she didn't exist !\033[00m")



def result_evo(nbr):
    nbr -= 1
    # If we want to change percentage of chance to evolve and/or bonus of evolution
    Perc_St = 25
    Perc_Li = 50
    UpStrength = 4
    UpLife = 2
    global cSB
    global cLB

    if random.randint(1, 100) <= Perc_St:
        cSB += UpStrength
    if random.randint(1, 100) <= Perc_Li:
        cLB += UpLife
    if nbr >= 1:
        result_evo(nbr)

"""
#------------------------------   TEST ------------------

def creacrea (Joueur):
    money = gaming_tools.get_player_money(Joueur)
    creaname = gaming_tools.get_random_creature_name()
    creavariety = gaming_tools.get_random_creature_variety()
    creastrength = random.randint(1,200)
    crealife = random.randint(1, 200)
    gaming_tools.set_creature(Joueur, creaname, creavariety, creastrength, crealife)

    txt = " "+Joueur+" ({}) get : "+creaname+""
    print(txt.format(money))
    txt =" [Type] : {} || [Strength] : {} / [Life] : {} \n-------"
    print(txt.format(creavariety,creastrength, crealife))
    return creaname


    #   ---   TEST   ---


# Creation d'un joueur et d'une créature pour le test
J1 = "Joueur1"
account.player_managment(J1)
crea1 = (creacrea(J1))

evolution(crea1,83)
"""