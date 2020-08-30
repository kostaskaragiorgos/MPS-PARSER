def getRanges(list):
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
    rangeName = []
    for i in rangelist:
        rangeName.append(i[4:12])
    return rangeName


def getRangesRestrictionName1(rangelist):
    rangerestname1 = []
    for i in rangelist:
        rangerestname1.append(i[14:22])
    return rangerestname1


def getRangesRestrictionValue1(rangelist):
    rangerestval1 = []
    for i in rangelist:
        rangerestval1.append(i[24:36])
    while("" in rangerestval1) : 
        rangerestval1.remove("")
    return rangerestval1

def getRangesRestrictionName2(rangelist):
    rangerestname2 = []
    for i in rangelist:
        rangerestname2.append(i[39:47])
    return rangerestname2

def getRangesRestrictionValue2(rangelist):
    rangerestval2 = []
    for i in rangelist:
        rangerestval2.append(i[49:61])
    while("" in rangerestval2) : 
        rangerestval2.remove("")
    return rangerestval2


def concatRange(list1, list2):
    return list1 + list2


from file import get_len_of_list, save_file_to_list

f = save_file_to_list("test.mps")
p = getRanges(f)

f = getRangeName(p)

rest1 = getRangesRestrictionName1(p)

val1 = getRangesRestrictionValue1(p)

for i in p:
    print(i)

for i in f:
    print(i)


for i in rest1:
    print(i)

for i in val1:
    print(i)