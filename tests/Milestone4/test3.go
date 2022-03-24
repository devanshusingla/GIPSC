package main

import "fmt"

var temp int = 3
var a [5]int = [5]int{temp + 1, temp + 2, temp / temp, temp + temp, temp * temp}
func Print(x, y int, z int) {}

func main() {
	var b, c, d int = a[0], a[1], a[2]
	Print(b, c, d)
}