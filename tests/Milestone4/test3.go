package main

import "fmt"

const temp int = 3
var b [temp+temp]int = [temp+temp]int{7, 8 }
var a [5]int = [5]int{temp + 1, temp + 2, temp / temp, temp + temp, temp * temp}
func Print(x, y int, z int) (int, int) {
	return x, y
}

func f2() (int, int) {
	return Print(1, 2, 3)
}

// func add(a, b int) (int) {
// 	return a + b
// }

func main() {
	var b, c, d int = a[0], a[1], a[2]
	var e, f int = Print(b, c, d)
	var x int  = b + c / d + c;
	f2()
	a := [5]int{1, 2, 3, 4, 5}
	s := a[1:4]
	// add(3, 5)
}