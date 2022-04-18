package main

import "fmt"

type point struct {
	x int
	y int
	e int
	fg int
	o int
}

func ars(v []point){
	(v[0]).x = 60
}

func ar(v point) {
	v.y = 40
}

func main() {
	var d point = point(4, 5,6 ,2 ,6)
	var arr []point = []point{d}
	ars(arr)
}
