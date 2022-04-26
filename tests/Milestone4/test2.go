package main

import "fmt"

var a [3]int = [3]int{1, 3, 5}
var b, c, d int = a[0], a[1], a[2]

func Print(x, y, z int) {}

func main() {
	for i := 0; i < 3; i++ {
		fmt.Scan_int(&a[i])
	}
	fmt.Print_int(b, c, d)
}