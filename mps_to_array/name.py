        
def getName(list):
    """
    returns the name of the mps file or sets it to NO NAME 
    input: list
    output:name
    """
    for i in list:
        if i[0:4] == "NAME":
            if  "" in i[14:22]:
                return "NO NAME"
            return i[14:22]

def get_type(list):
    """ returns the type of the problem """
    for i in list:
        if i[0:4] == "NAME":
            if "" in i[72:78]:
                return "MIN"
            return i[72:78]

def MinMax(type):
    """ returns a list 1x1 """
    MinMaxarr = []
    if type == "MIN":
        MinMaxarr.append(-1)
    elif type == "MAX":
        MinMaxarr.append(1)
    return MinMaxarr