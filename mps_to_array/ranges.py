def getRanges(list):
    """ Adds the ranges  to a list
    Args:
        A list.
    Returns:
        A list with the ranges. if no ranges found returns an empty list.
    """
    ranges= False
    Ranges = []
    for i in list:
        if (str(i[0:6]).upper() == "RANGES"):
            ranges = True
            continue
        if (str(i[0:6]).upper() == "ENDATA" or str(i[0:6]).upper() ==  "BOUNDS"):
            break
        if ranges == True:
            Ranges.append(i)
    return Ranges

def getRangeName(rangelist):
    """ Adds the name of every range to a list
    Args:
        A list with ranges
    Returns:
        A list with the names of  the ranges. if no ranges found returns an empty list.
    """
    rangeName = []
    for i in rangelist:
        rangeName.append(i[4:12])
    return rangeName


def getRangesRestrictionName1(rangelist):
    """ Adds the name of restriction 1 to a list
    Args:
        A list with ranges
    Returns:
        A list with the names of restriction 1. if no restrictions 1 found returns an empty list.
    """
    rangerestname1 = []
    for i in rangelist:
        rangerestname1.append(i[14:22])
    return rangerestname1


def getRangesRestrictionValue1(rangelist):
        """ Adds the values of restriction 1 to a list
    Args:
        A list with ranges
    Returns:
        A list with the values of restriction 1. if no restrictions 1 found returns an empty list.
    """
    rangerestval1 = []
    for i in rangelist:
        rangerestval1.append(i[24:36])
    while("" in rangerestval1) : 
        rangerestval1.remove("")
    return rangerestval1

def getRangesRestrictionName2(rangelist):
        """ Adds the name of restriction 2 to a list
    Args:
        A list with ranges
    Returns:
        A list with the names of restriction 2. if no restrictions 2 found returns an empty list.
    """
    rangerestname2 = []
    for i in rangelist:
        rangerestname2.append(i[39:47])
    return rangerestname2

def getRangesRestrictionValue2(rangelist):
    """ Adds the values of restriction 2 to a list
    Args:
        A list with ranges
    Returns:
        A list with the values of restriction 2. if no restrictions 2 found returns an empty list.
    """
    rangerestval2 = []
    for i in rangelist:
        rangerestval2.append(i[49:61])
    while("" in rangerestval2) : 
        rangerestval2.remove("")
    return rangerestval2


def concatRange(list1, list2):
    return list1 + list2

