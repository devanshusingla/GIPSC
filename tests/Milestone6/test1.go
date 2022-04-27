package main

import "fmt"

func add (a, b int) (int, int) {
	return a+b, a-b
}

func main() {
	// y := 6;
	// var x *int = &(y);
	// y = 2
	// var z int = 5
	a, b, c := 2,3 ,5
	fmt.Print_int(a)
	fmt.Print_int(b)
	fmt.Print_int(c)
	b, c, a = a, b, c
	fmt.Print_int(a)
	fmt.Print_int(b)
	fmt.Print_int(c)
	b, c, a = a, b, c
	fmt.Print_int(a)
	fmt.Print_int(b)
	fmt.Print_int(c)
}