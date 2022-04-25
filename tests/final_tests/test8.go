package main

import "fmt"

func f(x, y int) int {
	assign x = 2 
	assign y = 4
	return x + y
}

func main() {
	y := f(2, 4)

	if y < 5 {
		assign y = 8
		fmt.Print_int(y) 
	} else {
		assign y = 4
		fmt.Print_int(y)
	}

	for i := 0; i < 5; i++ {
		j := 1
		fmt.Print_int(i)
	}

}