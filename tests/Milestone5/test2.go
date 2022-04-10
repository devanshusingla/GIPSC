package main

import "fmt"

const a int = 2
const b int = a

const temp float64 = float64(a)

func add(a, b int) (int) {
	return a + b
}

func main() {
	x := int64(add(int(temp), int(temp + float64(2))))
}