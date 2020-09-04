
def getRHS(list):
    """ Adds the "rhses"  to a list
    Args:
        A list.
    Returns:
        A list with t
    """
    rhs= False
    RHS = []
    for i in list:
        if (str(i[0:3]).upper() == "RHS"):
            rhs = True
            continue
        if (str(i[0:3]).upper() == any(["ENDATA","RANGES","BOUNDS"])):
            break
        if rhs:
            RHS.append(i)
    return RHS

def getRpartName(rhslist):
    """ Adds the name of every "rhs" to a list
    Args:
        A list with rhses
    Returns:
        A list with the names of the "rhses". if no "rhses" found returns an empty list.
    """
    rpartname = []
    for i in rhslist:
        rpartname.append(i[4:12])
    return rpartname

def getRHSRestrictionName1(rhslist):
    """ Adds the name of restriction 1 to a list
    Args:
        A list with rhses
    Returns:
        A list with the names of restriction 1. if no restrictions 1 found returns an empty list.
    """
    rhsrestname1 = []
    for i in rhslist:
        rhsrestname1.append(i[14:22])
    return rhsrestname1

def getRHSRestrictionValue1(rhslist):
    """ Adds the values of restriction 1 to a list
    Args:
        A list with rhses
    Returns:
        A list with the values of restriction 1. if no restrictions 1 found returns an empty list.
    """
    rhsrestval1 = []
    for i in rhslist:
        rhsrestval1.append(i[24:36])
    while("" in rhsrestval1) : 
        rhsrestval1.remove("")
    return rhsrestval1


def getRHSRestrictionName2(rhslist):
    """ Adds the name of restriction 2 to a list
    Args:
        A list with rhses
    Returns:
        A list with the names of restriction 2. if no restrictions 2 found returns an empty list.
    """
    rhsrestname2 = []
    for i in rhslist:
        rhsrestname2.append(i[39:47])
    return rhsrestname2


def getRHSRestrictionValue2(rhslist):
    """ Adds the values of restriction 2 to a list
    Args:
        A list with rhses
    Returns:
        A list with the values of restriction 2. if no restrictions 2 found returns an empty list.
    """
    rhsrestval2 = []
    for i in rhslist:
        rhsrestval2.append(i[49:61])
    while("" in rhsrestval2) : 
        rhsrestval2.remove("")
    return rhsrestval2

def getb(list1, list2):
    return list1 + list2