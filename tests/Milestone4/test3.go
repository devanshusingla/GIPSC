package main

import "fmt"

var temp int = 3
var a [5]int = [5]int{temp + 1, temp + 2, temp / temp, temp + temp, temp * temp}
func Print(x, y int, z int) int {return x}

func add(a, b int) int {
	return a + b
}

func main() {
	var b, c, d int = a[0], a[1], a[2]
	var e int = Print(b, c, d)
	a := [5]int{1, 2, 3, 4, 5}
	s := a[1:4]
	add(3, 5)
}