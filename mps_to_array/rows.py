def getRows(list):
    """ saves the rows to a list
    input: list 
    return list
    """
    rows = []
    frows = False
    for i in list:
        if (str(i[0:4]).upper().strip(" ") == "ROWS"):
            frows = True
            continue
        if str(i[0:7]).upper() == "COLUMNS":
            break
        if frows:
            rows.append(i)
    return rows

def getRowNames(rowlist):
    """ 
    returns a list with the names of the rows
    input :list
    """
    rownames = []
    for i in rowlist:
        rownames.append (i[4:12])
    return rownames

def getRowType(rowlist):
    """ saves the row type to a list
    input: list
    output: row type
    """
    rowtype = []
    for i in rowlist:
        rowtype.append(i[1:3])
    return rowtype

def convertRowType(rowlist):
    """ converts row type
    input : rowlist
    return : converted rowlist """
    rowtypeconverted = []
    for i in rowlist:
        if str(i).upper() == "N":
            rowtypeconverted.append("OBJ")
        elif str(i).upper() == "E":
            rowtypeconverted.append(0)
        elif str(i).upper() == "G":
            rowtypeconverted.append(1)
        else:
            rowtypeconverted.append(-1)
    return rowtypeconverted

def getelementsofarow(columns,row):
    """ saves all the elements of a row """ 
    rowlist = []
    str(row).strip("\n")
    for i in columns:
        if str(i[14:22]).strip(" ") == row:
            rowlist.append(i[24:36])
        if str(i[39:47]).strip(" ") == row:
            rowlist.append(i[49:61])
    return rowlist

def findobj(rows):
    for i in rows:
        if str(i[1:3]).strip(" ").upper() == 'N':
            return (i[4:12])
