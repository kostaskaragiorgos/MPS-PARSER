
def getRHS(list):
    rhs= False
    RHS = []
    for i in list:
        if (str(i[0:3]).upper() == "RHS"):
            rhs = True
            continue
        if (str(i[0:6]).upper() == "ENDATA" or str(i[0:6]).upper() == "RANGES" or str(i[0:6]).upper() == "BOUNDS" ):
            break
        if rhs == True:
            RHS.append(i)
    return RHS

def getRpartName(rhslist):
    rpartname = []
    for i in rhslist:
        rpartname.append(i[4:12])
    return rpartname

def getRHSRestrictionName1(rhslist):
    rhsrestname1 = []
    for i in rhslist:
        rhsrestname1.append(i[14:22])
    return rhsrestname1

def getRHSRestrictionValue1(rhslist):
    rhsrestval1 = []
    for i in rhslist:
        rhsrestval1.append(i[24:36])
    while("" in rhsrestval1) : 
        rhsrestval1.remove("")
    return rhsrestval1


def getRHSRestrictionName2(rhslist):
    rhsrestname2 = []
    for i in rhslist:
        rhsrestname2.append(i[39:47])
    return rhsrestname2


def getRHSRestrictionValue2(rhslist):
    rhsrestval2 = []
    for i in rhslist:
        rhsrestval2.append(i[49:61])
    while("" in rhsrestval2) : 
        rhsrestval2.remove("")
    return rhsrestval2

def getb(list1, list2):
    return list1 + list2