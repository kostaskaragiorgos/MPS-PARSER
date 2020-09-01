def getColumns(list):
    """ Adds the columns  to a list
    Args:
        A list.
    Returns:
        A list with the columns. if no columns found returns an empty list.
    """
    columns = []
    cls = False
    for i in list:
        if (str(i[0:7]).upper() == "COLUMNS"):
            cls = True
            continue
        if str(i[0:3]).upper() == "RHS":
            break
        if (cls == True):
            columns.append(i)
    return columns

def getColVarName(columnlist):
    """ Adds the names   of every column to a list
    Args:
        A list with the columns
    Returns:
        A list with the name of every column. if no columns found returns an empty list.
    """
    colvarnames= []
    for i in columnlist:
        colvarnames.append(i[4:12])
    return colvarnames


def getColRestrictionName1(columnlist):
    """ Adds the name of restriction 1 to a list
    Args:
        A list with the columns
    Returns:
        A list with the names of restriction 1. if no restrictions 1 found returns an empty list.
    """
    colrestname1 = []
    for i in columnlist:
        colrestname1.append(i[14:22])
    return colrestname1

def getColRestrictionValue1(columnlist, objname):
    """ Adds the values of restriction 1 to a list
    Args:
        A list with columns
        A name of a row
    Returns:
        A list with the values of restriction 1. if no restrictions 1 found returns an empty list.
    """
    colrestval1 = []
    objname = str(objname).strip("\n")
    for i in columnlist:
        if str(i[14:21]).strip(" ") == objname:
            continue
        colrestval1.append(i[24:36])
    return colrestval1

def getColRestrictionName2(columnlist):
    """ Adds the name of restriction 2 to a list
    Args:
        A list with the columns
    Returns:
        A list with the names of restriction 2. if no restrictions 2 found returns an empty list.
    """
    colrestname2 = []
    for i in columnlist:
        colrestname2.append(i[39:47])
    return colrestname2

def getColRestrictionValue2(columnlist, objname):
        """ Adds the values of restriction 2 to a list
    Args:
        A list with columns
        A name of a row
    Returns:
        A list with the values of restriction 2. if no restrictions 1 found returns an empty list.
    """
    colrestvalue2 = []
    objname = str(objname).strip("\n")
    for i in columnlist:
        if str(i[39:46]).strip(" ") == objname:
            continue
        colrestvalue2.append(i[49:61])
    return colrestvalue2

def getColVarNameFromRest(columnlist,restrictionname):
    """
    Saves the variable name based on restriction name
    Args:
        columnlist: a list with columns
        restrictionname: the name of the restriction
    Returns:
        A list of variable names.if none returns an empty list.
    """
    restrictionname = str(restrictionname).strip("\n")
    colvarnamesfromobj= []
    for i in columnlist:
        if str(i[39:46]).strip(" ") == str(restrictionname).strip(" ") or str(i[14:21]).strip(" ") == (restrictionname).strip(" "):
            colvarnamesfromobj.append(i[4:12])
    return colvarnamesfromobj

def getA(list1, list2):
    return list1 + list2
