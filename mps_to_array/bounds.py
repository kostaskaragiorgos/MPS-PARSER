def getBounds(list):
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
    boundtype = []
    for i in boundlist:
        boundtype.append(i[1:3])
    return boundtype

def getBoundName(boundlist):
    boundnames= []
    for i in boundlist:
        boundnames.append(i[4:12])
    return boundnames


def getBoundsRestrictionName1(boundlist):
    boundsrestname1 = []
    for i in boundlist:
        boundsrestname1.append(i[14:22])
    return boundsrestname1


def getBoundsRestrictionValue1(boundlist):
    boundrestval1 = []
    for i in boundlist:
        boundrestval1.append(i[24:36])
    while("" in boundrestval1) : 
        boundrestval1.remove("")
    return boundrestval1

def getBoundsRestrictionName2(boundlist):
    boundsrestname2 = []
    for i in boundlist:
        boundsrestname2.append(i[39:47])
    return boundsrestname2

def getBoundsRestrictionValue2(boundlist):
    boundsrestval2 = []
    for i in boundlist:
        boundsrestval2.append(i[49:61])
    while("" in boundsrestval2) : 
        boundsrestval2.remove("")
    return boundsrestval2


def concatBounds(list1, list2):
    return list1 + list2
