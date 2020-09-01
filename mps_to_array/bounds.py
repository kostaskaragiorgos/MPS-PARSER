def getBounds(list):
    """ Adds the bounds  to a list
    Args:
        A list.
    Returns:
        A list with the bounds. if no bounds found returns an empty list.
    """
    bounds= False
    Bounds = []
    for i in list:
        if (str(i[0:6]).upper() == "BOUNDS"):
            bounds = True
            continue
        if (str(i[0:6]).upper() == "ENDATA"):
            break
        if bounds == True:
            Bounds.append(i)
    return Bounds

def getBoundtype(boundlist):
    """ Adds the bound type of every bound to a list
    Args:
        A list with bounds
    Returns:
        A list with the type of bounds. if no bounds found returns an empty list.
    """
    boundtype = []
    for i in boundlist:
        boundtype.append(i[1:3])
    return boundtype

def getBoundName(boundlist):
    """ Adds the name of every bound to a list
    Args:
        A list with bounds
    Returns:
        A list with the names of bounds. if no bounds found returns an empty list.
    """
    boundnames= []
    for i in boundlist:
        boundnames.append(i[4:12])
    return boundnames


def getBoundsRestrictionName1(boundlist):
    """ Adds the name of restriction 1 to a list
    Args:
        A list with bounds
    Returns:
        A list with the names of restriction 1. if no restrictions 1 found returns an empty list.
    """
    boundsrestname1 = []
    for i in boundlist:
        boundsrestname1.append(i[14:22])
    return boundsrestname1


def getBoundsRestrictionValue1(boundlist):
    """ Adds the values of restriction 1 to a list
    Args:
        A list with bounds
    Returns:
        A list with the values of restriction 1. if no restrictions 1 found returns an empty list.
    """
    boundrestval1 = []
    for i in boundlist:
        boundrestval1.append(i[24:36])
    while("" in boundrestval1) : 
        boundrestval1.remove("")
    return boundrestval1

def getBoundsRestrictionName2(boundlist):
    """ Adds the name of restriction 2 to a list
    Args:
        A list with bounds
    Returns:
        A list with the names of restriction 2. if no restrictions 2 found returns an empty list.
    """
    boundsrestname2 = []
    for i in boundlist:
        boundsrestname2.append(i[39:47])
    return boundsrestname2

def getBoundsRestrictionValue2(boundlist):
    """ Adds the values of restriction 2 to a list
    Args:
        A list with bounds
    Returns:
        A list with the values of restriction 2. if no restrictions 2 found returns an empty list.
    """
    boundsrestval2 = []
    for i in boundlist:
        boundsrestval2.append(i[49:61])
    while("" in boundsrestval2) : 
        boundsrestval2.remove("")
    return boundsrestval2


def concatBounds(list1, list2):
    return list1 + list2
