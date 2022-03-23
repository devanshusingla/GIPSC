package main

import "fmt"

var a [2]int32 = [2]int32{1.0, 2}

func Print(x int) {}

func main() {
	c := a[0] + a[1]
}