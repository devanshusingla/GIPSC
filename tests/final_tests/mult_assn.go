package main

import "fmt"

func main() {
	a := 1
	b := 2
	assign a, b = a+b, a-b
	fmt.Print_int(a)
	fmt.Print_int(b)

	c := 5
	d := 9
	assign c, d = d+2, c+2*d
	fmt.Print_int(c)
	fmt.Print_int(d)
}