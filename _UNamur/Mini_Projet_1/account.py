
import gaming_tools

def player_managment(name):
    """
    Check if player exists else create it.
    
    Parameters
    ----------
    name : player name (Str)
    Raises
    -------
       Value error : Player already exists
    """

    if gaming_tools.player_exists(name) :
        playermoney = gaming_tools.get_player_money(name)
        txt = "Player "+ name + " already exists and has {} credits."
        print(txt.format(playermoney))
        if gaming_tools.has_creature(name):
            print ("And the player have already a creature. \n")
        #print ("Would you like to create a new player ?")
    else :
        gaming_tools.add_new_player(name)
        gaming_tools.set_player_money(name,225)
        print ("Player "+ name + " is created with 225 credits.")
