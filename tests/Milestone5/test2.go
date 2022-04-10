package main

import "fmt"

const temp float64 = float64(3)

func add(a, b int) (int) {
	return a + b
}

func main() {
	var x int64 = int64(add(int(temp), int(temp + float64(2))))
}