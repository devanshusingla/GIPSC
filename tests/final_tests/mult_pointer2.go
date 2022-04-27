package main

import "fmt"

func inc(x int) (int, int) {
	assign x = x + 6
	var z int=5
	return z, x+3
}

func main() {
	z,a := inc(5)
	y := 6;
	var x *int = &(y);
	assign y = 2
	assign *(&y) = 4
	var g *int = &y;

	var p int = 2
	var a1 int = 5
	var a2 *int = &a1
	var a3 **int = &a2
	var a4 ***int = &a3
	var r ****int = &a4
	fmt.Print_int(****r)
	assign ***r = &p
	fmt.Print_int(****r)
	fmt.Print_int(y)
}