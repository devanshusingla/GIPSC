package main

import (
	"fmt"
	"math"
)

func cos(x float64 ) float64 {
	return math.Sin(math.PI/2 - x);
}

func main() {
	x := cos(2.2)
	y := 7.8
	y += cos(x)
}