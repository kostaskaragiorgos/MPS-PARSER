def getColumns(list):
    """
    returns the columns
    input: list
    output: list
    """
    columns = []
    cls = False
    for i in list:
        if (i[0:7] == "COLUMNS"):
            cls = True
            continue
        if (cls == True and i[0:3] != "RHS"):
            columns.append(i)
        if i[0:3] == "RHS":
            break
    return columns

def getColVarName(columnlist):
    colvarnames= []
    for i in columnlist:
        colvarnames.append(i[4:12])
    return colvarnames


def getColRestrictionName1(columnlist):
    colrestname1 = []
    for i in columnlist:
        colrestname1.append(i[14:22])
    return colrestname1

def getColRestrictionValue1(columnlist, objname):
    colrestval1 = []
    objname = objname.strip("\n")
    for i in columnlist:
        if str(i[14:21]).strip(" ") == objname:
            continue
        colrestval1.append(i[24:36])
    return colrestval1

def getColRestrictionName2(columnlist):
    colrestname2 = []
    for i in columnlist:
        colrestname2.append(i[39:47])
    return colrestname2

def getColRestrictionValue2(columnlist, objname):
    colrestvalue2 = []
    objname = objname.strip("\n")
    for i in columnlist:
        if str(i[39:46]).strip(" ") == objname:
            continue
        colrestvalue2.append(i[49:61])
    return colrestvalue2

def getA(list1, list2):
    return list1 + list2