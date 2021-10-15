import gaming_tools 

def sell_creature(creature_name):
    """
    Parameters
    ----------
    creature_name: name of the creature 

    raises:
    ------
    ValueError: player doesn't has any creature
    ValueError: player's name does not exist 

    """

    if gaming_tools.creature_exists(creature_name):

        player = gaming_tools.get_player(creature_name)
        money = gaming_tools.get_player_money(player)
        strength = gaming_tools.get_creature_strength(creature_name)
        life = gaming_tools.get_creature_life(creature_name)

        money = (strength+life)*0.5 + money

        gaming_tools.set_player_money(player, money)

        gaming_tools.remove_creature(creature_name)

        print ("your total money is" , money )
        print ("The buy is done")
    else:
        print("\033[0;31m   => This creature didn't exist\033[00m")

    
