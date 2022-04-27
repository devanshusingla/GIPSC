package main

import "fmt"

type Address struct {
	a, b int
	d [10]int
}

func main() {
	var x1 Address
	x1.a = 4
	x1.b = 34
	x1.d[0] = 3

	fmt.Print_int(x1.a)
}