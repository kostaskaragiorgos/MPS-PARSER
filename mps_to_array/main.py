import sys
from file import save_file_to_list
from name import get_type, MinMax
from columns import getColRestrictionValue1, getColRestrictionValue2, getA
from rows import getRows, convertRowType, getRowType, getelementsofarow, findobj
from rhs import getRHS, getb, getRHSRestrictionValue1, getRHSRestrictionValue2
from columns import getColumns

def savefile(outputfile, tosave):
    columns = getColumns(tosave)
    rows = getRows(tosave)
    objname = findobj(rows)
    A1 = getColRestrictionValue1(columns,objname)
    A2 = getColRestrictionValue2(columns, objname)
    rhs = getRHS(tosave)
    rhs1 = getRHSRestrictionValue1(rhs)
    rhs2 = getRHSRestrictionValue2(rhs)
    rowtype = getRowType(rows)
    problem_type = get_type(tosave)
    with open(outputfile,'w') as f:
        f.write(str(MinMax(problem_type))+'\n')
        f.write(str(getelementsofarow(columns,str(objname).strip('\n')))+'\n')
        f.write(str(A1))
        f.write(str(A2))
        f.write(str(convertRowType(rowtype))+'\n')
        f.write(str(getb(rhs1,rhs2))+'\n')

def main():
    if len(sys.argv) < 3:
        print("The arguments should be the script name , a .mps file as an input file and a .txt file as an output file")
        sys.exit(1)
    else:
        script = sys.argv[0]
        filename = sys.argv[1]
        outputfile = sys.argv[2]
    if filename.endswith(".mps") and outputfile.endswith(".txt"):
        a = save_file_to_list(filename)
        savefile(outputfile, a)
    elif not filename.endswith(".mps"):
        print("Input file needs to be .mps file")
        sys.exit(1)
    else:
        print("Output file needs to be .txt file")
        sys.exit(1)

if __name__ == '__main__':
   main()
