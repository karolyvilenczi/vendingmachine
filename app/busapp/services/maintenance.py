from busapp.apputils.app_logger import applog

# Checks
def coin_opener_check():
    """
        Checks if the coin door is OK.
    """
    applog.debug("Checking if the coin door is OK.")
    
    # ACTUAL CHECK NOT IMPLEMENTED
    return True

def spring_rotary_motors_check():
    """
        Checks if the motor behind each spring is OK.
    """
    applog.debug("Checking if the motor behind each spring is OK.")
    
    # ACTUAL CHECK NOT IMPLEMENTED
    return True


def goods_serving_bay_check():
    """
        Checks if the lever where the goods fall opens.
    """
    applog.debug("Checking if the serving bay door opens.")
    
    # ACTUAL CHECK NOT IMPLEMENTED
    return True


def lights_are_up_check():
    """
        Checks if the lights work.
    """
    applog.debug("Checking if the lights work.")
    # ACTUAL CHECK NOT IMPLEMENTED        
    return True


def front_door_is_locked():
    """
        Checks if the front_door_is_locked
    """
    applog.debug("Checking if the front door is locked.")
    # ACTUAL CHECK NOT IMPLEMENTED
    return True


def coin_is_valid():
    """
        Checks if the coin inserted is in fact a coin and is valid.
    """
    applog.debug("Checking if coin inserted is valid.")
    # ACTUAL CHECK NOT IMPLEMENTED
    return True


def open_tresor_bay():
    """"
    Opens the tresor bay at the end of sale
    """
    applog.debug("Opening the tresor bay at the end of sale")
    # ACTUAL ACTION NOT IMPLEMENTED
    return True

def save_coins_to_tresor_bay():
    """"
    Saves coin to the bay.
    """
    applog.debug("Saved coin to the bay.")
    # ACTUAL ACTION NOT IMPLEMENTED
    return True
    
def close_tresor_bay():
    """"
    Closes the tresor bay at the end of sale
    """
    applog.debug("Closing the tresor bay at the end of sale")
    # ACTUAL ACTION NOT IMPLEMENTED
    return True



def return_all_coins_to_return_bay():
    """"
    Reurns all coins to the return bay
    """
    applog.debug("Returned all coins to the return bay")
    # ACTUAL ACTION NOT IMPLEMENTED
    return True

# etc.


# Maintenance scrips
def open_front_door():
    applog.info("Opening front door.")
    return True

def open_tresor():
    applog.info("Opening tresor.")
    return True
