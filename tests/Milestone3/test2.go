package main;
import (
    "fmt";
    "math/rand";
    "time";
);

type Node struct {
    value int;
    sub_tree_sum int;
    flag bool;
    left *Node;
    right *Node;
    parent *Node;
};
func visit(nodeptr *Node) int {
    if nodeptr == nil {
        return 0;
    }
    node := *nodeptr;
    (*nodeptr).sub_tree_sum += visit(node.left);
    if node.flag {
        (*nodeptr).sub_tree_sum += visit(node.right);
    } else {
        (*nodeptr).sub_tree_sum -= visit(node.right);
    }
    if node.parent != nil{
        (*nodeptr).sub_tree_sum *= node.parent.value;
    }
    return (*nodeptr).sub_tree_sum;
};
func main(){
    var n int = 20;
    var max_val int = 100;
    graph := make([]Node, n+1);
    rand.Seed(time.Now().UnixNano());
    // Initialise value for the binary tree;
    for i := 1; i<=n; i++{
        graph[i].value = rand.Intn(max_val);
        graph[i].sub_tree_sum = graph[i].value;
        if rand.Intn(2) == 1 {
            graph[i].flag = true;
        } else {
            graph[i].flag = false;
        };
        if i*2 <= n {
            graph[i].left = &graph[i*2];
        } else {
            graph[i].left = nil;
        };
        if i*2 +1 <= n {
            graph[i].right = &graph[i*2 + 1];
        } else {
            graph[i].right = nil;
        };
        graph[i].parent = &graph[i/2];
    };
    graph[1].parent = nil;
    // Traversing the tree recursively;
    visit(&graph[1]);
    // Printing subtree sum;
    for i := 1; i<=n; i++ {
        fmt.Println(" Subtree Sum for ", i, " = ",graph[i].sub_tree_sum);
    };
}