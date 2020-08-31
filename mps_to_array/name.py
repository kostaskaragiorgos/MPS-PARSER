def getName(list):
    """
    returns the name of the mps file or sets it to NO NAME 
    input: list
    output:name
    """
    for i in list:
        if str(i[0:4]).upper() == "NAME":
            if  "" in i[14:22]:
                return "NO NAME"
            return i[14:22]

def get_type(list):
    """ returns the type of the problem """
    for i in list:
        if str(i[0:4]).upper() == "NAME":
            return i[73:77]

def MinMax(type):
    """ returns a list 1x1 """
    MinMaxarr = []
    if  "MAX" in type:
        MinMaxarr.append(1)
    else:
        MinMaxarr.append(-1)
    return MinMaxarr

def MinMaxString(type):
    if "MAX" in str(type).upper():
        return "Max"
    return "Min"