""""

Diviser en différentes fonctions


"""
import gaming_tools, random


def combat(crea1,crea2):

    print(" *-*-*-*  COMBAT  *-*-*-*")
    # ---   Get playerowner, variety, strength and life of the 2 creatures   ---
    player1 = gaming_tools.get_player(crea1)
    player2 = gaming_tools.get_player(crea2)
    varcrea1 = gaming_tools.get_creature_variety(crea1)
    varcrea2 = gaming_tools.get_creature_variety(crea2)
    resultcombat = 0
    tempcrea1_strength = gaming_tools.get_creature_strength(crea1)
    tempcrea2_strength = gaming_tools.get_creature_strength(crea2)
    tempcrea1_life = gaming_tools.get_creature_life(crea1)
    tempcrea2_life = gaming_tools.get_creature_life(crea2)

    # ---   Test best variety ---

    if (varcrea1 == varcrea2) :
        resultcombat = 0
        signe = "="
        print(" ** Variety are the same  **")
    elif (varcrea1 == "fire" and varcrea2 == "water") or (varcrea1 == "water" and varcrea2 == "plant") or (varcrea1 == "plant" and varcrea2 == "fire") :
        resultcombat = -1
        signe = "<"
        print("  **  Variety "+varcrea2+" of "+crea2+" is the best.  **")
    else :
        #(varcrea1 == "fire" and varcrea2 == "plant") or (varcrea1 == "water" and varcrea2 == "fire") or (varcrea1 == "plant" and varcrea2 == "water")
        resultcombat = 1
        signe = ">"
        print("  **  Variety " + varcrea1 + " of " + crea1 + " is the best.  **")

    #   --- Strength adaptation if necessary   ---
    if resultcombat == 1:
        tempcrea1_strength = tempcrea1_strength*2
    else :
        #resultcombat == -1
        tempcrea2_strength = tempcrea2_strength *2

    #   --- COMBAT   ---
    print("----------------------------")
    print("|   "+player1+"   |   "+player2+"  |")
    print("|-------------|------------|")
    print("| "+ crea1 +"  | " +crea2 +"  |")
    print("|    "+varcrea1+"    \033[0;31m"+signe+"\033[00m    "+varcrea2+"    |")
    print("|    [S]trength & [L]ife   |")
    txt = "|  S:{}/L:{}  | S:{}/L:{} |"
    print(txt.format(tempcrea1_strength, tempcrea1_life, tempcrea2_strength, tempcrea2_life))
    print("----------------------------")

    tempcrea2_life = tempcrea2_life - tempcrea1_strength
    if tempcrea2_life < 0:
        tempcrea2_life = 0
    txt = " " + crea1 + " deals {} to " + crea2 + "."
    print(txt.format(tempcrea1_strength))
    tempcrea1_life = tempcrea1_life - tempcrea2_strength
    if tempcrea1_life < 0:
        tempcrea1_life = 0
    txt = " "+crea2+" deals {} to "+crea1+"."
    print(txt.format(tempcrea2_strength))




    #   ---   Result   ---
    winmoney = 50
    loosemoney = 0
    tempmoneyplayer1 = gaming_tools.get_player_money(player1)
    tempmoneyplayer2 = gaming_tools.get_player_money(player2)

    if tempcrea1_life == 0 :
        print (""+crea1+" \033[0;31mdied\033[00m \n" +crea2+" won the fight")
        # delete la creature 1
        gaming_tools.remove_creature(crea1)
        # Joueur 2 reçoit 50 crédits et joueur 1 reçoit 0 crédits
        tempmoneyplayer2 += 50
        gaming_tools.set_player_money(player2, tempmoneyplayer2)
        txt = "" +player2+" owner of " + crea2 + " win {} credits. " + player1 + " get {} credits."
        print(txt.format(winmoney, loosemoney))
    elif tempcrea2_life == 0 :
        print (" "+crea2+" \033[0;31mdied\033[00m \n"+crea1+" won the fight")
        # delete la creature 2
        gaming_tools.remove_creature(crea2)
        # Joueur 1 reçoit 50 crédits et joueur 2 reçoit 0 crédits
        tempmoneyplayer1 += 50
        gaming_tools.set_player_money(player1,tempmoneyplayer1)
        txt = ""+player1+" owner of "+crea1+" win {} credits. "+player2+" get {} credits."
        print(txt.format(winmoney, loosemoney))
    elif tempcrea1_life > tempcrea2_life :
        gaming_tools.set_creature_life(crea1,tempcrea1_life)
        print (""+crea1+" won the fight ")
        # Joueur 1 reçoit 50 crédits et joueur 2 reçoit 0 crédits
        tempmoneyplayer1 += 50
        gaming_tools.set_player_money(player1, tempmoneyplayer1)
        txt = "" + player1 + " owner of " + crea1 + " win {} credits. " + player2 + " get {} credits."
        print(txt.format(winmoney, loosemoney))
    elif tempcrea2_life > tempcrea1_life :
        gaming_tools.set_creature_life(crea2, tempcrea2_life)
        print (""+crea2+" won the fight ")
        # Joueur 2 reçoit 50 crédits et joueur 1 reçoit 0 crédits
        tempmoneyplayer2 += 50
        gaming_tools.set_player_money(player2, tempmoneyplayer2)
        txt = "" + player2 + " owner of " + crea2 + " win {} credits. " + player1 + " get {} credits."
        print(txt.format(winmoney, loosemoney))
    else :
        print ("Draw \n")
        # Each player get 10 credits
        tempmoneyplayer2 += 10
        tempmoneyplayer2 += 10
        gaming_tools.set_player_money(player1, tempmoneyplayer1)
        gaming_tools.set_player_money(player2, tempmoneyplayer2)
        print(" "+player1+" and "+player2+" won 10 credits each.")

    #Mettre les 2 set player money ici ?


# -------------------------------------------------------------------
# -------------------------------------------------------------------
#   ---   Fonction creation creatures pour tester le combat   ---

    # Creation de 2 creatures pour le tester
"""
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


# Creation de 2 joueurs pour le test
J1 = "Joueur1"
J2 = "Joueur2"

gaming_tools.add_new_player(J1)
gaming_tools.add_new_player(J2)


# Génération de 2 créatures
print (" \n Génération de 2 créatures \n--------------------\n")

crea1 = (creacrea(J1))
crea2 = (creacrea(J2))

#   ---   COMBAT   ----
print ("Combat")

combat(crea1,crea2)
"""