from parser import buildAndCompile
from codegen import MIPS
import sys, os

if(len(sys.argv)) != 2:
    exit()
path_name = sys.argv[1]

parsed_output, sym_table = buildAndCompile(path_name)

codegen = MIPS()
mips = codegen.tac2mips(parsed_output, sym_table)

print(mips)
with open(path_name[:-3]+'.s', 'w') as f:
    for ins in mips:
        f.write(ins)
        f.write('\n')