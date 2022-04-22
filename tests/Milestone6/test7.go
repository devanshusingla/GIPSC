package main

// import "fmt"

func f(x, y int) int {
	x = 2 
	y = 4
	return x + y
}

func main() {
	y := f(2, 4)

	if y < 5 {
		y = 6 
	} else {
		y = 4
	}

	for i := 0; i < 5; i++ {
		j := 1
	}
}