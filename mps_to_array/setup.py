from file import save_file_to_list
from name import get_type, MinMax
from columns import getColRestrictionValue1, getColRestrictionValue2, getA
from rows import getRows, convertRowType, getRowType, getelementsofarow, findobj
from rhs import getRHS, getb, getRHSRestrictionValue1, getRHSRestrictionValue2
from columns import getColumns

def input_mps_file(filename):
    problemlist = save_file_to_list(filename)
    columns = getColumns(problemlist)
    rows = getRows(problemlist)
    objname = findobj(rows)
    A1 = getColRestrictionValue1(columns,objname)
    A2 = getColRestrictionValue2(columns, objname)
    #B
    rhs = getRHS(problemlist)
    rhs1 = getRHSRestrictionValue1(rhs)
    rhs2 = getRHSRestrictionValue2(rhs)
    #Eqin
    rowtype = getRowType(rows)
    #MinMax
    problem_type = get_type(problemlist)

    
def save_to_txt_file(filename):
    with open(filename,'w') as f:
        f.write(str(MinMax(problem_type))+'\n')
        f.write(str(getelementsofarow(columns,str(objname).strip('\n')))+'\n')
        f.write(str(A1))
        f.write(str(A2)+'\n')
        f.write(str(convertRowType(rowtype))+'\n')
        f.write(str(getb(rhs1,rhs2))+'\n')
