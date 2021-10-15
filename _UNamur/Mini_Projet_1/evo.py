


#Fonction d'évolution sa créature
sampleList = [1, 1, 0, 2]   # 1 represente la chance d'augumenter sa vie de 2 , 0 represente la chance d'augumenter sa force et 1 represente les deux chances 
x = random.choice(sampleList)



def evolution(name_player,credit,creature) :
    if name_player == gaming_tools.get_player(creature) : # verifier si le joueur a cette creature
        if gaming_tools.get_player_money(name_player) >= 10 :  # verifier si l'argent est suffisant pour evoluer
            if credit == 10 :
                if x == 0 : # alors on va augumenter la force
                     newstrength = gaming_tools.get_creature_strength(creature)+4
                     gaming_tools.set_creature_strength(creature,newstrength)
                     print("NEW STRENGTH ! : ", gaming_tools.get_creature_strength(creature))
                if x == 1 :  # on va augumenter la vie 
                     newlife = gaming_tools.get_creature_life(creature)2 
                     gaming_tools.set_creature_life(creature,newlife)
                     print("NEW life ! : ", gaming_tools.get_creature_life(creature))
                if x == 2 : # on va augumenter les deux a la fois 
                     newstrength = gaming_tools.get_creature_strength(creature)4
                     newlife = gaming_tools.get_creature_life(creature)2
                     gaming_tools.set_creature_strength(creature,newstrength)
                     gaming_tools.set_creature_life(creature,newlife)
                     print("NEW life ! : ", gaming_tools.get_creature_life(creature)," AND STRENGTH : ", gaming_tools.get_creature_strength(creature))
            else : 
                print("10 CREDIT !!! ")
        else: 
                print("you don't have enough money to evoluate ! ")
    else : 
        print("this player ",name_player," don't have this creature ",creature)