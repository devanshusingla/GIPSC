from parser import buildAndCompile
import sys, os

from scope import NodeListNode

if not os.path.exists(sys.argv[1]):
    print("Invalid Path to Source Code")
    sys.exit(1)
ast = buildAndCompile(sys.argv[1])
if ast is None:
    sys.exit(1)
path_to_source_file = sys.argv[1][:-3]
node_ids = [f'\t0 [label={ast}];']
print(f"Saving to {path_to_source_file}.dot ...")
with open(f"{path_to_source_file}.dot", 'w') as f:
    f.write("digraph G {\n")
    def dfs(node, id):
        global node_ids
        if hasattr(node, 'children') and node.children is not None:
            for i, c in enumerate(node.children):
                if isinstance(c, list):
                    c = NodeListNode(c)
                    node.children[i] = c
                node_ids.append(f'\t{len(node_ids)} [label="{c}"];')
                f.write(f'\t{id} -> {len(node_ids)-1};\n')
                dfs(c, len(node_ids)-1)

    dfs(ast,0)
    f.writelines(node_ids)

    f.write("\n}")