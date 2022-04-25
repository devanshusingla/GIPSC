package main

import "fmt"

type myStruct struct {
	x, y int
}

func main() {
	var a myStruct 
	a.x = 2
	a.y = 4

	fmt.Print_int(a.x + a.y)
	fmt.Print_int(a.x * a.y)

}