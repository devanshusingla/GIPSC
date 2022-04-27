package main

import "fmt"

type Address struct {
	a, b int
	c *int
	d rune
}

func main() {
	var x1 Address
	assign x1.a = 4
	assign x1.b = 34

	fmt.Print_int(x1.a)
}