package main

import "fmt"

func f(x int) int {
	return x
}

func main() {
	y := f(2)

	if y < 5 {
		y = 6 
	} else {
		y = 4
	}
}