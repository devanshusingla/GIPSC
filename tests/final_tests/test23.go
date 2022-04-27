package main

import (
	"fmt"
	"math"
)

func main(){
	var a, b int
	var c int
	fmt.Scan_int(&a)
	fmt.Scan_int(&b)
	math.Square(a, &c)
	fmt.Print_int(c)
	math.Cube(b, &c)
	fmt.Print_int(c)
	assign c = math.IsPrime(78)
	fmt.Print_int(c)
}