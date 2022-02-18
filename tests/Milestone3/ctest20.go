package main
import "fmt"
type node struct {
	val int
	l   struct *node
	r   struct *node
}
var nil node
func inorder(head *node) {
	if (head == &nil) {
		return
	}
	bst((*head).l)
	print((*head).val,"\n")
	bst((*head).r)
}

func main() {

	var a1 node
	a1.val = 1
	var a2 node
	a2.val = 2
	var a3 node
	a3.val = 3
	var a4 node
	a4.val = 4
	var a5 node
	a5.val = 5

	var head *node
    head=&a1
	a1.l = &a2
	a1.r = &a3
	a2.l = &a4
	a2.r = &a5
	a3.l = &nil
	a3.r = &nil
	a4.l = &nil
	a4.r = &nil
	a5.l = &nil
	a5.r = &nil

	inorder(head)
}
