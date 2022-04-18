package main

import "fmt"

const b int = 3
var x int = 7
var y int = x + 3
var a string = string(b)

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