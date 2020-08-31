import sys
from mps_to_array.file import save_file_to_list
from mps_to_array.name import get_type, MinMax, MinMaxString
from mps_to_array.columns import getColRestrictionValue1, getColRestrictionValue2, getA
from mps_to_array.rows import getRows, convertRowType, getRowType, getelementsofarow, findobj
from mps_to_array.rhs import getRHS, getb, getRHSRestrictionValue1, getRHSRestrictionValue2
from mps_to_array.columns import getColumns, getColVarNameFromRest
from mps_to_array.ranges import getRanges, getRangesRestrictionValue1, getRangesRestrictionValue2, concatRange
from mps_to_array.bounds import getBounds, getBoundsRestrictionValue1 , getBoundsRestrictionValue2, concatBounds

def savefile(outputfile, tosave):
    problem_type = get_type(tosave)
    columns = getColumns(tosave)
    rows = getRows(tosave)
    objname = findobj(rows)
    objvarnames = getColVarNameFromRest(columns, objname)
    rowelemenents = getelementsofarow(columns,str(objname).strip('\n'))
    objectivefunction = [i+ j for i , j in zip(rowelemenents, objvarnames)]
    with open(outputfile,'w') as f:
        f.write(str(MinMaxString(problem_type)))
        f.write(str(objectivefunction)+'\n')
        f.write("S.T \n")
        
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
