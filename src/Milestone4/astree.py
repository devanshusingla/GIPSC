from parser import parse

ast = parse()
node_ids = [f'\t0 [label={ast}];']
with open("test.dot", 'w') as f:
    f.write("digraph G {\n")
    def dfs(node, id):
        global node_ids
        if hasattr(node, 'children') and node.children is not None:
            # print(f'{node.children}')
            for c in node.children:
                node_ids.append(f'\t{len(node_ids)} [label={node}];')
                f.write(f'\t{id} -> {len(node_ids)-1};\n')
                dfs(c, len(node_ids)-1)

    dfs(ast,0)
    f.writelines(node_ids)

    f.write("\n}")