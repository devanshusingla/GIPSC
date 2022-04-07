package main

import "fmt"

const temp int = 3

// func add(a, b int) (int) {
// 	return a + b
// }

func main() {
	*(&(temp)) = 8
}