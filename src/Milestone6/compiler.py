from parser import buildAndCompile
from codegen import MIPS
import sys, os

if(len(sys.argv)) != 2:
    exit()
path_name = sys.argv[1]

parsed_output, sym_table = buildAndCompile(path_name)

with open(f"{path_name[:-3]}_3ac.txt", 'w') as f:
    for line in parsed_output.code:
        f.write(line)
        f.write("\n")

codegen = MIPS(parsed_output.code, sym_table)
mips = codegen.tac2mips()

# print(mips)
with open(path_name[:-3]+'.s', 'w') as f:
    for ins in mips:
        f.write(ins)
        f.write('\n')

