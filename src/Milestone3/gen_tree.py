import sys
import ast

if(len(sys.argv) != 2):
    print("Provide the path to generated tree file")
    sys.exit(1)

path_to_tree = sys.argv[1]
path_to_dot = '.'.join(path_to_tree.split('.')[:-1])+".dot"

fdot= open(path_to_dot,"w")
fdot.write("digraph ParseTree {")
fdot.write("\n")

def writeGraph(outerList, stateId):
    currentStateId=stateId
    nextStateId=stateId+1
    name=outerList[0]
    if(len(outerList) > 1):
        for innerList in outerList[1:]:
            if(len(innerList)>0):
                # Label Current Vertex
                fdot.write(str(currentStateId) + "[label=\"" + str(name) + "\"]; ")
                if ((innerList[0][0])=="\""):
                    innerList[0]=innerList[0][1:-1]
                # Label Next Vertex
                fdot.write(str(nextStateId) + "[label=\"" + str(innerList[0]) + "\"]; ")
                # Mark Edge from Current Vertex to Next Vertex 
                # Edge from Outer List to Inner List
                fdot.write(str(currentStateId) + "->" + str(nextStateId) + " ;\n")
                nextStateId = writeGraph(innerList, nextStateId)
    return nextStateId

with open(path_to_tree, 'r') as ftree:
    writeGraph(ast.literal_eval(ftree.read()), 0)

fdot.write("}")
fdot.close()
