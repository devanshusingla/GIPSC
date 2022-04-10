package main

// import "fmt"

var a int = 3

func Print(x int) {}

func main() {
	var b []int = []int{1,2,6,8}
	c := b[0] + b[1]
	b[1]++
	d := c + 5

	for d < 5 {
		d -= 1
	}

	Print(d)
}